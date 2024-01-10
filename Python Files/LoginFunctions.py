# Import
import sqlite3
from sqlite3 import Error
import datetime
from datetime import datetime
import pandas as pd
import json as J
import flask as F
from flask import jsonify

# -------------------------- #

# Functions


def JsonToDict();
    
    


# Query Database using Query build
def QueryDB(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    JsonFile(result[0])


# Ensuring Stability of JSON



# -------------------------- #
