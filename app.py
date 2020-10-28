from flask import Flask, jsonify

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
from config import password

# SET UP THE DATABASE

# variables to populate the database connection string
db_user = 'postgres'
db_password = password
db_host = 'localhost'
db_port = 5432
# This database must already exist
db_name = 'covid_ETL'

engine = create_engine(f'postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# reflect exisiting database into a new model
Base = automap_base()

# reflect tables
Base.prepare(engine, reflect=True)
covid_result = Base.classes.covid_table


# Flask SET UP

app = Flask(__name__)

# Flask Routes
@app.route('/')
def home():


    session = Session(engine)

    results = session.query(covid_result.state, covid_result.date, covid_result.code, covid_result.death, covid_result.total_cases).all()

    session.close()

    return jsonify(results)


if __name__ =='__main__':
    app.run(debug=True)
