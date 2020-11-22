# sqlalchemy-challenge

The purpose of this challenge is to conduct some climate analysis using Python and SQLAlchemy and then use Flask to generate a web based API interface to view the data and to allow the user to define the date range for data queries to return temperature observations. 


### Documents in this repository are:

* climate_Bowen.ipynb - My Jupyter Notebook file running a Python 3 kernel that contains the SQLAlchmey, Pandas, and Matplotlib code for conducting the data analysis and plotting the results

* climateApp.py - My Python file running that contains the Flask Apps and python code to generate the Web based API

* images folder - contains images of the query and WebPage outputs

* Resources folder - contains the data files of the climate and observation station data used for the analysis


***
### Design concept:

## Step 1: 

Part one uses SQLAlchemy within Jupyter Notebook to reflect data tables into SQLAlchemy ORM, automap the table keys and perform a query and analysis to determine precipitation over a one year period. The analysis starts with querying the database to determine the last date and then calculating the data one year earlier. This data is then used to query the database for precipitation data for all dates after the calculated date.The data is sorted by date and summary statistics of the data are generated.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture7.png)  ![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture10.png)

The results were then grouped the determine the average precipitation by date and plotted using both:  
### Pandas.plot.bar  
![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture8.png)

### Matplotlib plt.bar  
![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture9.png)

***
Part two of the challenge continues with another query to gather data on the weather observation stations and temperature observations.

The first query is simply to count the number of observation sttions in the database.
![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture11.png)

The next analysis involved querying two different tables to gather station id, station name, and temperature observation data and then merging the dataframes based on the station id values present in both databases. The resulting dataframe is then grouped, counted, and sorted to determine the number of observations made by each observation station.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture12.png)

A query of the station with the most recorded observations is made and saved to a pandas dataframe. The min, max and average temperature is determined.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture13.png)

A query based on the past year using the query date determined in part one is used to generate a histogram of the temperature observations from the station.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture14.png)


***
## Step 2:

Step two uses Flask to create apps to generate web based queries of the database and relys on reusing much of the python code from step one to conduct the analysis.

### HomePage App

Simply generates a list of available app options for the user to choose from.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture1.png)

### Precipitation App

Opens a query session, conducts a query to to gather date and precipitation data, closes the query, reads the data into a dictionary using the date value as the key and precipitation as the values, then uses json to display the dictionary to the web page.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture2.png)

### Stations App

Opens a query session, conducts a query to to gather station ids and station names, closes the query, reads each row of data into a dictionary using the id value as the key and name as the values, appends each dictionary to a list of all stations, then uses json to display the list to the web page.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture3.png)

### Tobs App

Opens a query session, reuses the 1 year date query and calculation from Part one of Step one, conducts a second query to gather station and temperature observations over the last year, calculates the station with the most observations using the process from Part two of Step one, conducts a third query to import the temperature data over the past year from the station with the most observations, closes the query, appends each teperature value to a list of all temperature observations, then uses json to display the list to the web page.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture4.png)

### start_date App

This App requires the user to enter a start date in the format %Y-%m-%d in the browser header, opens a query session, uses the SQLAlchemy functions (func.min, func.avg, and func.max) to conduct a query of all temperature observations with a filter of only retrieving observation dates greater than or equal to a user defined start date, closes the query, creates a dictionary of the results using (min, average, and max) as keys, then uses json to display the dictionary to the web page.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture5.png)

### end_date App

This App follows the same steps as the start_date App, but requires the user to provide second date in the browser header. The query uses the second date as a filter to only retrieve observation dates less than or equal to this user defined end date.

![alt tag](https://github.com/robertjbowen/sqlalchemy-challenge/blob/main/images/Picture6.png)
