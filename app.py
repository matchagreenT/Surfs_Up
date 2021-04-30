from flask import Flask, jsonify

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

export FLASK_APP=app.py

set FLASK_APP=app.py

flask run

localhost:5000
    