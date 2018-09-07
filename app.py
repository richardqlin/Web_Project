from flask import Flask
from flask import render_template

from database import Database

from routes.api import api 

import requests

app=Flask(__name__)

app.register_blueprint(api)

@app.before_first_request
def initialize_database():
	Database.initialize()

@app.route('/')
def index():
	entries = requests.get('https://murmuring-bastion-31969.herokuapp.com/entries').json()
	return render_template('index.html', entries = entries)

@app.route('/add')
def add_entry():
	return render_template('add_entry.html')

if __name__=="__main__":
	app.run(debug=True)
