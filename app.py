##### App Utilities
import os
import env
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, current_app, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
    
    
@app.route('/edit_tweet/<tweet_id>')
def edit_tweet(tweet_id):
    the_tweet = mongo.db.tweets.find_one({"_id": ObjectId(tweet_id)})
    all_hashtags = mongo.db.hashtags.find()
    return render_template('edit_tweet.html', tweet = the_tweet, hashtags = all_hashtags)
    
    
@app.route('/update_tweet/<tweet_id>', methods=['POST'])
def update_tweet(tweet_id):
    tweets = mongo.db.tweets
    tweets.update( {'_id': ObjectId(tweet_id)},
                    {
                    'tweet_hashtag' : request.form.get['hashtag'],
                    'tweet_retweets' : request.form.get['retweets'],
                     'tweet_text' : request.form.get['text'],
                     'tweet_date' : request.form.get['date']
                    })
    return redirect(url_for('get_tweets'))   
    
    
@app.route('/delete_tweet/<tweet_id>')
def delete_tweet(tweet_id):   
    mongo.db.tweets.remove({"_id": ObjectId(tweet_id)})
    return redirect(url_for('get_tweets')) 
                    
                    
@app.route('/get_hashtags')
def get_hashtags():
    _hashtags = mongo.db.hashtags.find()
    return render_template('get_hashtags.html', hashtags = _hashtags)
    
    
@app.route('/edit_hashtag/<hashtag_id>')
def edit_hashtag(hashtag_id):   
    the_hashtag = mongo.db.hashtags.find_one({"_id": ObjectId(hashtag_id)})
    return render_template('edit_hashtag.html', hashtag = the_hashtag)        
    
@app.route('/delete_hashtag/<hashtag_id>')
def delete_hashtag(hashtag_id):   
    mongo.db.hashtags.remove({"_id": ObjectId(hashtag_id)})
    return redirect(url_for('get_hashtags'))     


## APP INITIATION

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 

