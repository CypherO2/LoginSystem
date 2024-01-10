from flask import Flask, jsonify, request
from flask_cors import CORS

# ~ DOCSTRING ~
"""
    This server needs to be run locally.
    When running, it can be accessed through localhost:5000.
"""
# app = Flask function - name as variable fed into function
app = Flask(__name__)
# Cross Origin Resourse Sharing - manually define who can send information to server
# CORS function from flask_cors : (see line 10), resource = {regex"anywhere/thing" : {(data can be sent from anywhere)}}
CORS(app, resources={r"/*": {"origins": "*"}})

# app (see Line 10) with condition route @ "/staff", & method == "GET" ( Decoration of JSON - decribe a function '@' )
@app.route("/staff", methods=["GET"])
# declare function to return JSON to client
def get_staff():
    return jsonify(staff)


# if name == main ( proper industry practice )
if __name__ == "__main__":
    # app ( see Line 10 ) . run (0 variables)
    app.run()