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
 - `tweet_ids` - Tweet ids of tweets sharing the news. This field is list of tweet ids separated by tab


## Installation

###  Requirements:
Data download scripts are writtern in python and requires `python 3.8+` to run.

Install all the libraries in `requirements.txt` using the following command:
````
pip install -r requirements.txt
````


## Running Code

### Virtual Environment setup:
Create the virtual environment:
````
> py -3 -m venv venv
````

Activate the corresponding environment:
````
> venv\Scripts\activate
````

### Flask setup:
Configure flask environment:
````
> $env:FLASK_ENV = "development"
> $env:FLASK_APP = "get_results.py"
````

After the setup, run the following command to launch the flask app:
````
> flask run
````


## References
If you use this dataset, please cite the following papers:
~~~~
@article{shu2018fakenewsnet,
  title={FakeNewsNet: A Data Repository with News Content, Social Context and Dynamic Information for Studying Fake News on Social Media},
  author={Shu, Kai and  Mahudeswaran, Deepak and Wang, Suhang and Lee, Dongwon and Liu, Huan},
  journal={arXiv preprint arXiv:1809.01286},
  year={2018}
}
~~~~
~~~~
@article{shu2017fake,
  title={Fake News Detection on Social Media: A Data Mining Perspective},
  author={Shu, Kai and Sliva, Amy and Wang, Suhang and Tang, Jiliang and Liu, Huan},
  journal={ACM SIGKDD Explorations Newsletter},
  volume={19},
  number={1},
  pages={22--36},
  year={2017},
  publisher={ACM}
}
~~~~
~~~~
@article{shu2017exploiting,
  title={Exploiting Tri-Relationship for Fake News Detection},
  author={Shu, Kai and Wang, Suhang and Liu, Huan},
  journal={arXiv preprint arXiv:1712.07709},
  year={2017}
}
~~~~


[Fake News Detection on Social Media: A Data Mining Perspective](https://arxiv.org/abs/1708.01967) </br>
[Exploiting Tri-Relationship for Fake News Detection](http://arxiv.org/abs/1712.07709) </br>
[FakeNewsTracker](http://blogtrackers.fulton.asu.edu:3000)
[FakeNewsNet](https://arxiv.org/abs/1809.01286)

(C) 2019 Arizona Board of Regents on Behalf of ASU