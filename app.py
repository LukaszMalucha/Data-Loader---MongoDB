##### App Utilities
import os
import env
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, current_app, request, redirect, url_for, flash
from flask_pymongo import PyMongo


##### App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") 
Bootstrap(app)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") 


mongo = PyMongo(app)


@app.route('/')
# @app.route('/home')
# def home():
    
#     return render_template("home.html")
@app.route('/get_tweets')
def get_tweets():
    _tweets=mongo.db.tweets.find()
    tweets_list = [tweet for tweet in _tweets]
    return render_template("get_tweets.html", tweets=tweets_list)
    
    
@app.route('/add_tweet')
def add_tweets():
    _hashtags = mongo.db.hashtags.find()
    hashtag_list = [hashtag for hashtag in _hashtags]
    return render_template("add_tweets.html", hashtags= hashtag_list)
    
@app.route('/insert_tweet', methods=['POST'])
def insert_tweet():
    tweets=mongo.db.tweets
    tweets.insert_one(request.form.to_dict())
    return redirect(url_for('get_tweets'))




## APP INITIATION

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 

