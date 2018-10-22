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
    return render_template("tweets.html", tweets=mongo.db.tweets.find())
    
    
@app.route('/add_tweet')
def add_tweets():
    
    return render_template("add_tweets.html")
    





## APP INITIATION

# if __name__ == '__main__':
#     # Bind to PORT if defined, otherwise default to 5000.
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port, debug=True) 


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    