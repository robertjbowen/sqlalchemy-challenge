# sqlalchemy-challenge

The purpose of this challenge is to conduct some climate analysis using Python and SQLAlchemy and then use Flask to generate a web based interface to view the data and to allow the user to define the date rrange for data queries to return temperature observations. 


### Documents in this repository are:

* climate_Bowen.ipynb - My Jupyter Notebook file running a Python 3 kernel that contains the SQLAlchmey, Pandas, and Matplotlib code for conducting the data analysis and plotting the results

* data directory containing the source file of purchasing data - purchase_data.csv

* images folder - contains images of the code blocks and their outputs

* Checkpoints directory containing checkpoint .ipynb files

***
### Design concept:

## Step 1: 

Part one uses SQLAlchemy within Jupyter Notebook to reflect data tables into SQLAlchemy ORM, automap the table keys and perform a query and analysis to determine precipitation over a one year period. The analysis starts with querying the database to determine the last date and then calculating the data one year earlier. This data is then used to query the database for precipitation data for all dates after the calculated date.The data is sorted by date and summary statistics of the data are generated.

![alt tag](link to picture 7)  ![alt tag](link to picture 10)

The results were then grouped the determine the average precipitation by date and plotted using both: 
Pandas.plot.bar 
![alt tag](link to picture 8)

Matplotlib plt.bar 
![alt tag](link to picture 9)

***
Part two of the challenge continues with another query to gather data on the weather observation stations and temperature observations.

The first query is simply to count the number of observation sttions in the database.
![alt tag](link to picture 11)

The next analysis involved querying two different tables to gather station id, station name, and temperature observation data and then merging the dataframes based on the station id values present in both databases. The resulting dataframe is then grouped, counted, and sorted to determine the number of observations made by each observation station.

![alt tag](link to picture 12)

A query of the station with the most recorded observations is made and saved to a pandas dataframe. The min, max and average temperature is determined.

![alt tag](link to picture 13)

A query based on the past year using the query date determined in part one is used to generate a histogram of the temperature observations from the station.

![alt tag](link to picture 14)


***
## Step 2:

Step two uses Flask to create apps to generate web based queries of the database and relys on reusing much of the python code from step one to conduct the analysis.

### HomePage App

Simply generates a list of available app options for the user to choose from.

![alt tag](link to picture 1)

### Precipitation App

Opens a query session, conducts a query to to gather date and precipitation data, closes the query, reads the data into a dictionary using the data value as the key and precipition as the values, then uses json to display the dictionary to the web page.

![alt tag](link to picture 2)

### Precipitation App

Opens a query session, conducts a query to to gather date and precipitation data, closes the query, reads the data into a dictionary using the data value as the key and precipition as the values, then uses json to display the dictionary to the web page.

![alt tag](link to picture 2)

