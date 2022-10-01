from flask import Flask, redirect, url_for, render_template, request
import random
import string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect(':memory:')

c = conn.cursor()
c.execute("""CREATE TABLE friends (
            code text,
            name text,
            location blob,
            markers interger
            )""")

conn.commit()
conn.close()


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


