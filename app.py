##### App Utilities
import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, current_app, request, redirect, url_for, flash



##### App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdasdasd'
Bootstrap(app)


@app.route('/')
@app.route('/home')
def home():
    
    return render_template("home.html")





## APP INITIATION

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 