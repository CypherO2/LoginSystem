from flask import Flask, jsonify, request
from flask_cors import CORS

# import LoginFunctions as LF
import sqlite3
from sqlite3 import Error

# app = Flask function - name as variable fed into function
app = Flask(__name__)
# Cross Origin Resourse Sharing - manually define who can send information to server
# CORS function from flask_cors : (see line 10), resource = {regex"anywhere/thing" : {(data can be sent from anywhere)}}
CORS(app, resources={r"/*": {"origins": "*"}})

logins = {}
@app.route("/login", methods=["POST"])
def login_details():
    print("Request Recieved")
    with sqlite3.connect(
        r"\\scc-fs-hf4\Students$\stu2223\S301389\Year2 Py\Project\LoginSystem\Database Files\CustomerStaffLogin.db"
    ) as conn:
        username = request.json.get("username")
        # print(username)
        password = request.json.get("password")
        try:
            cu = conn.cursor()
            query = """Select * From users Where Username = ?"""
            cu.execute(query, (username,))
            results = cu.fetchall()
            # print(results)
            for i in results:
                logins[i[3]] = i[4]
                print(logins)
                print(logins[username])
            if password == logins[username]:
                return jsonify({"success":True, "message": "Login Successful"})
            else:
                return jsonify({"success":False, "message": "Incorrect Login Details"}),400
        except Exception as e:

            print(e)
            return jsonify({"sucess": False, "message": "Incorrect Login Details"}), 400


# if name == main ( proper industry practice )
if __name__ == "__main__":
    # app ( see Line 10 ) . run (0 variables)
    app.run()

# if __name__ == "__main__":
#     app.run(ssl_context="adhoc")
