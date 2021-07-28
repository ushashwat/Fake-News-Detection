# Fake News Detection
This project aims to detect Fake News on Twitter based on a user query and display the results on a webpage using Flask.


## Dataset overview
FakeNewsNet contains 2 datasets collected using ground truths from Politifact and Gossipcop. The minimalistic version of this dataset provided by FakeNewsNet includes the following files:

 - `politifact_fake.csv` -  Samples related to fake news collected from PolitiFact 
 - `politifact_real.csv` -  Samples related to real news collected  from PolitiFact 
 - `gossipcop_fake.csv` - Samples related to fake news collected from GossipCop
 - `gossipcop_real.csv` - Samples related to real news collected from GossipCop

Each of the above CSV files is comma separated file and has the following columns:

 - `id` - Unique identifider for each news
 - `url` - Url of the article from web that published that news 
 - `title` - Title of the news article
 - `tweet_ids` - Tweet ids of tweets sharing the news. This field is list of tweet ids separated by tab.


## Installation

###  Requirements:
Data download scripts are writtern in python and requires `python 3.8 +` to run.

Install all the libraries in `requirements.txt` using the following command
````
pip install -r requirements.txt
````


## Running Code

### Virtual Environment setup:
Create the virtual environment:
````
py -3 -m venv venv
````

Activate the corresponding environment:
````
venv\Scripts\activate
````

### Flask setup:
Configure flask environment:
````
> $env:FLASK_ENV = "development"
> $env:FLASK_APP = "get_results.py"
````