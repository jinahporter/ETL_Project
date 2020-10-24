from flask import Flask, jsonify

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as import pdb; pdb.set_trace()

#SET UP THE DATABASE

#create engine
engine = create_engine('')

#reflect exisiting database into a new model
Base = automap_base()

#reflect tables
Base.prepare(engine, reflect=True)

#Flask SET UP 

app = Flask(__name__)

#Flask Routes
@app.route('/')
def home():
    return(

    )

@app.route('/api/v1.0/<country_name>')
def country_name():
    session = Session(engine)

    #whatever we need to put in here:

    session.close()

@app.route('/api/v1.0/weather'

if __name__ = '__main__':
    app.run(debug=True)