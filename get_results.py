# importing the required libraries
from flask import Flask, render_template, request, redirect, url_for
from joblib import load

# load the pipeline object
pipeline = load("fake_news_classification.joblib")

# function to get the result for a particular text query
def requestResults(name):
    return str(pipeline.predict(name))


# start flask
app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method is detected, redirect to success function
@app.route('/', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        user = request.form['search']
        return redirect(url_for('success', name=user))

# get the data for the requested query
@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "