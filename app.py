from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#holds index html, base page


# this is all the pages stuff

@app.route('/map')

