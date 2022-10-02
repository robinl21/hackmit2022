from flask import Flask, redirect, url_for, render_template, request
import random
import string
from datetime import datetime
import sqlite3
import json

app = Flask(__name__)


conn = None

try:
    conn = sqlite3.connect('friends.db', check_same_thread=False)
except Error as e:
    print(e)


create_friends_table = """CREATE TABLE IF NOT EXISTS friends (
                                    code text NOT NULL,
                                    name text NOT NULL,
                                    longitude real,
                                    latitude real,
                                    avatar blob
                                );"""
c = conn.cursor()
c.execute(create_friends_table)
conn.commit()

# flask runs each function when at the site corresponding to route
@app.route('/', methods=["POST", "GET"])
def index():
    print("TEST")
    print(request.form)
    print(request.form.keys())
    if request.method == "POST":
        if 'previousSession' in request.form.keys(): #user has session code
            input_Code = request.form['existingCode']
            
            #if no code input: reset page, since won't be able to access inputname url
            if request.form['existingCode'] == '':
                return render_template('index.html', error_message="Please input a valid code!")

            #otherwise redirect to input name
            return redirect(url_for("inputname", code=input_Code)) #sends to inputname/code
        
        else: #user wants to create new code
            #random code, redirect to input name
            input_Code = ''
            for x in range(6):
                input_Code += random.choice(string.ascii_uppercase + string.digits)
            return redirect(url_for("inputname", code=input_Code))
    else:
        return render_template('index.html', error_message="")

#holds index html, base page
@app.route('/inputname/<code>', methods=["POST", "GET"]) #pass in code as parameter
def inputname(code):
    #form submission with user code, asks for name
    if request.method == "POST":
        print(request.form)
        return redirect(url_for("studyspace", code=code, name=request.form["userName"])) #redirects to study space
    else:
        return render_template('input_name.html', code=code)

@app.route('/studyspaces/<code>/<name>', methods=["POST", "GET"]) #pass in name/code
def studyspace(code, name):
    #save code, name, location, into database
    return render_template('study_spaces.html', code=code, name=name)

# Given a student's information, store it in the database
@app.route('/enterinfo', methods=["POST", "GET"])
def enter_info():
    if request.method == "POST":
        
        params = [request.form["code"], request.form["name"], request.form["latitude"], request.form["longitude"]]
        for i in range(len(params)):
            params[i] = '\'' + params[i] + '\''

        sql_command = ', '.join(params) + ", \'SLAY\'"
        c.execute("PRAGMA table_info(friends)")
        items = c.fetchall()
        for item in items:
            print(item)
        print("HI")
        query1 = "INSERT INTO friends (code, name, longitude, latitude, avatar) VALUES(" + sql_command + ")"
        c.execute(query1)
        conn.commit()

        print(c.fetchall())
        return "HI"

@app.route('/removeinfo', methods=["POST", "GET"])
def remove_info():
    if request.method == "POST":
        params = [request.form["code"], request.form["name"], request.form["latitude"], request.form["longitude"]]
        for i in range(len(params)):
            params[i] = '\'' + params[i] + '\''

        sql_command = ', '.join(params) + ", \'SLAY\'"

        query1 = "DELETE FROM friends WHERE code=" + params[0] + "AND name=" + params[1]
        c.execute(query1)
        conn.commit()

        return "HI"

        

# Given a code, return all items in the database with the same code value
@app.route('/getcodefriends', methods=["POST", "GET"])
def get_code_friends():
    if request.method == "POST":
        params = [request.form["code"]]
        for i in range(len(params)):
            params[i] = '\'' + params[i] + '\''
        code = params[0]
        query1 = "SELECT code, name, longitude, latitude, avatar FROM friends WHERE code =" + code
        print(query1)
        result = c.execute(query1) 
        result = result.fetchall()
        result = json.dumps(result)

    return result