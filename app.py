import os
from dotenv import load_dotenv
from flask_debugtoolbar import DebugToolbarExtension
import git
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_behind_proxy import FlaskBehindProxy

load_dotenv()
app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
