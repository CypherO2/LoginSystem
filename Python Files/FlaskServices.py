from flask import Flask, jsonify, request
from flask_cors import CORS
import cryptography
from bcrypt import checkpw, gensalt, hashpw
# import LoginFunctions as LF
import sqlite3
from sqlite3 import Error
import re

# app = Flask function - name as variable fed into function
app = Flask(__name__)
# Cross Origin Resourse Sharing - manually define who can send information to server
# CORS function from flask_cors : (see line 10), resource = {regex"anywhere/thing" : {(data can be sent from anywhere)}}
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/login", methods=["POST"])
def login_details():
    logins = {}
    print("Request Recieved")
    with sqlite3.connect(
        r"\\scc-fs-hf4\Students$\stu2223\S301389\Year2 Py\Project\LoginSystem\Database Files\LoginSignup.db"
    ) as conn:
        print("Connection Established")
        username = request.json.get("username")
        if len(username) < 5:
            return jsonify({"success": False, "message": "Username is not long enough"})
        elif len(username) > 16:
            return jsonify({"success": False, "message": "Username is to long"})
        elif not username.isalnum():
            return jsonify({"success": False, "message": "Username is Not Alphanumeric"})
        # print(username)
        password = request.json.get("password")
        if len(password) < 5:
            return jsonify({"success": False, "message": "Password Not Long Enough"})
        elif len(password) > 16:
            return jsonify({"success": False, "message":"Password to Long"})
        password = password.encode("utf-8")
        try:
            cu = conn.cursor()
            print("Cursor Created")
            query = """Select * From users Where Username = ?"""
            cu.execute(query, (username,))
            results = cu.fetchall()
            print(results)
            for i in results:
                logins[i[3]] = i[4]
                print(logins)
                print(logins[username])
            if checkpw(password, logins[username]):
                return jsonify({"success":True, "message": "Login Successful", "Festive Message": "Blessed Yuletide"})
            else:
                return jsonify({"success":False, "message": "Incorrect Login Details"}),400
        except Exception as e:
            print(e)
            return jsonify({"success": False, "message": "Incorrect Login Details"}), 400

@app.route("/signup", methods=["POST"])
def signup_details():
    print("Request Recieved")
    with sqlite3.connect(
        r"\\scc-fs-hf4\Students$\stu2223\S301389\Year2 Py\Project\LoginSystem\Database Files\LoginSignup.db"
    ) as conn:
        print("Connection Established")
        name = request.json.get("name")
        dob = request.json.get("dob")
        username = request.json.get("username")
        if len(username) < 5:
            return jsonify({"success": False, "message": "Username is not long enough"})
        elif len(username) > 16:
            return jsonify({"success": False, "message": "Username is to long"})
        elif not username.isalnum():
            return jsonify({"success": False, "message": "Username is Not Alphanumeric"})
        count = """Select Count(Username) From users Where Username = ?"""
        cu = conn.cursor()
        print("Cursor Created")
        cu.execute(count,(username,))
        results = cu.fetchall()
        for i in results:
            if int(i[0]) > 1:
                return jsonify({"success": False, "message": "Username is Taken"})
        password = request.json.get("password")
        if len(password) < 5:
            return jsonify({"success": False, "message": "Password Not Long Enough"})
        elif len(password) > 16:
            return jsonify({"success": False, "message":"Password to Long"})
        password = password.encode("utf-8")
        # confirmPass = request.json.get("confirmPass").encode("utf-8")
        # if password == confirmPass:
        salt = gensalt()
        hashedPassword = hashpw(password, salt)
        try:
            
            statement = """INSERT INTO users(Name, DOB, Username, Password) VALUES(?,?,?,?)"""
            cu.execute(statement,(name, dob, username, hashedPassword))
            conn.commit()
            return jsonify({"success": True, "message": "Signup Successful", "Festive Message": "Blessed Yuletide"})
        except:
            print("Value could not be added to DB")
            return jsonify({"success": False, "message": "Internal Server Error"}),500
        # else:
        #     return jsonify({"success": False, "message": "Passwords Do NOT Match"})




if __name__ == "__main__":
    app.run()
    #ssl_context="adhoc"
