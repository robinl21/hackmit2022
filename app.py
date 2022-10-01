from flask import Flask, render_template

app = Flask(__name__)
# flask runs each function when at the site corresponding to route
@app.route('/')
def index():
    return render_template('index.html')

#holds index html, base page


# this is all the pages stuff


