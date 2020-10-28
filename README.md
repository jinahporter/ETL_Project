# ETL_Project

Project Proposal: https://docs.google.com/document/d/1kmT6UE7WvCXS1mBW_B0wwX_YNX_DiqTbhMbWWVPYULA/edit?usp=sharing

Datasets:
* https://covidtracking.com/data/api
* https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days (used as a CSV file)

## Final Report

### Data Sources
We selected data from Covid Tracking and the CDC as the data sets provided from both sites had the most breadth of data for states, cases, total deaths. We did want to make sure we used two separate sources, as the CDC data could be considered controversial due to the lack of reporting in its data set as well. With COVID Tracking, the data was derived from a more reputable source, Johns Hopkins, and has a very clean dataset to work with, which is constantly and consistently being updated. 

### ETL Process
We first used the data from Covid Tracking’s API to call in the data and the specific items we needed - which was confirmed deaths and dates for each specific state. In the other set, we used a CSV from the CDC to gather the total number of cases per each state.  Looking at both data sets, we could see that the states were labeled differently - either in the abbreviated form or in the full name form, so it is also helpful to note that we also grabbed a data set from Kaggle that has all of the states and abbreviations in a CSV format. 

When transforming the data derived from each site, we wanted to use the data sets and simplify them without the extraneous data. For example, the CDC data has a “Probable Death” column, and death rates per groups of people, which is data that we don’t necessarily need. Additionally, there are US territories - Guam, Puerto Rico, American Samoa, that we are intentionally not keeping in our data set as well as we are only focusing on the data within the continent and Hawaii. With the data, we did merge the state CSV and Covid Tracking Data with an inner merge so that only the 50 states + D.C. would be captured with the data set and also return both State Name and State Abbreviation and State Code.  We did a second merge with the CDC data set with the newly merged data in order to query the State Code, the date, the number of deaths, more state information, and total cases. Finally, we then kept only a few columns as some of the state information was repetitive in the data set and renamed the column values so that when used in SQL, would be easy to reference and would match. 

Lastly, to load the data into the database, we decided to use a PostgreSQL database for storage, as the data is structured. 

### Transformation Process 
The transformation that was performed to remove the extraneous information - as mentioned before “Probable Causes”, “Case Rate for 100K per day”, “Deaths in the last 7 days”, etc., that would not necessarily give our data set more standing. Ultimately, the data retained is meant to give a summary of deaths and cases per state. 

### Use of SQL Database 
Ultimately, with the amount of data queried and the structure that we had with numerical values, there was no need to use a NoSQL database and could handle complex queries much in a faster, transactional manner. The data set created would be able to create functions to aggregate numbers if need be, and also could potentially be updated regularly with the structure set in place.

### Table Schema
![table](https://github.com/jinahporter/ETL_Project/blob/main/covid%20data%20ERD.png)
With the way the data set was designed, we created one table within the database that would be able to hold all of the information, with the State Code as the Primary ID per each State. 

### Hypothetical use case(s) for database
What this dataset could do if it were set to pull and write data, queries could be used to pull what the number of cases was per State and per each date. Additionally, one could use this information to identify case/death trends in each state for growth or decreases over a period of time. 
