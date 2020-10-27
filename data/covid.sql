DROP TABLE covid_table

CREATE TABLE covid_table (
	state VARCHAR NOT NULL,
    date DATE NOT NULL,
	code VARCHAR(2) NOT NULL PRIMARY KEY,
	death INT NOT NULL,
	total_cases INT NOT NULL 
);

SELECT *
FROM covid_table;