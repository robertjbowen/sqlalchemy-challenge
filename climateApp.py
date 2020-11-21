# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:09:35 2020

@author: Rob Bowen
"""

import numpy as np
import pandas as pd
from datetime import datetime
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask('climate_app')


#################################################
# Flask Routes
#################################################

@app.route("/")
def homePage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and precipitation scores"""
    # Perform a query to retrieve the date and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data
    precipitation_dict = {}
    for date, prcp in results:
       precipitation_dict[date] = prcp 
    
    # Display the json dictionary   
    return jsonify(precipitation_dict)
    


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of station id numbers and names"""
    # Query all station ids and names
    results2 = session.query(Station.station, Station.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for stat, title in results2:
        station_dict = {}
        station_dict[stat] = title
        all_stations.append(station_dict)
    #Display the list of Stations    
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of station id numbers and temperature observations"""
    # Query the last date in the DB
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # Convert the value to a string and clean unnessary characters
    date_str = str(last_date).replace(',','').replace('(','').replace(')','').replace("'",'')
    # convert string to a datetime object and calulate the date 1 year earlier
    date = datetime.strptime(date_str, "%Y-%m-%d")
    query_date = date - dt.timedelta(days=365)
    
    # Query all station ids and temps for the last year
    results3 = session.query(Measurement.station, Measurement.tobs).filter(Measurement.date >= query_date).all()

    # Save the query results as a Pandas DataFrame
    station_obs = pd.DataFrame(results3, columns=['station','tobs'])
    #Group by stations and determine the number of total observations for each sorted most to fewest
    active_stations = station_obs.groupby(['station']).count()
    active_stations = active_stations.sort_values(by=['tobs'], ascending=False)
    # Determine the station with the most observations over the past year
    station_max = active_stations.index[0]
    
    # Query the temp measurements for the station with the most observations over the last year
    results4 = session.query(Measurement.tobs).filter(Measurement.station == station_max).filter(Measurement.date >= query_date).all()
    
    session.close()
    # Create a list and append each temperature observation to it
    all_tobs = []
    for tobs in results4:
        all_tobs.append(tobs)
    #Display the temperature observations for the previous year
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>") 
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of max, average, and min temperature observations since start date"""
    # Query the DB
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    results5 = session.query(*sel).filter(func.strftime("%Y-%m-%d", Measurement.date) >= start).all()
    
    session.close()
    
    # Create a dictionary and append each temperature observation to it
    sel_temps = {'min':results5[0][0],'average':results5[0][1],'max':results5[0][2]}
        
    #Display the temperature observations for the range
    return jsonify(sel_temps)

@app.route("/api/v1.0/<start>/<end>") 
def end_date(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of max, average, and min temperature observations within the date range"""
    # Query the DB
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    results6 = session.query(*sel).filter(func.strftime("%Y-%m-%d", Measurement.date) >= start).filter(func.strftime("%Y-%m-%d", Measurement.date) <= end).all()
    
    session.close()
   
    # Create a dictionary and append each temperature observation to it
    rng_temps = {'min':results6[0][0],'average':results6[0][1],'max':results6[0][2]}
        
    #Display the temperature observations for the range
    return jsonify(rng_temps)
    
if __name__ == '__main__':
    app.run(debug=True)


