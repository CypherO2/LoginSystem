#Import
import sqlite3
from sqlite3 import Error
import datetime
from datetime import datetime
import pandas as pd
import json as J
import flask as F
from flask import jsonify
# -------------------------- #

#Functions

def JsonToDict();
    with open("query.json") as jsonFile:
        jsonDict = J.load(jsonFile)

# -------------------------- #