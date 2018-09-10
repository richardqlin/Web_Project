from flask import Flask
from flask import render_template,redirect,url_for,request

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

@app.route('/add',methods=['GET','POST'])
def add_entry():

	if request.method=='POST':

		data={
		'title':request.form['title'],
		'post':request.form['post']
		}
		Database.insert_record(data)
		requests.post('https://murmuring-bastion-31969.herokuapp.com/post',data=data)
		return redirect(url_for('index'))
	
	return render_template('add_entry.html')

	
@app.route('/clear',methods=['DELETE'])
def delete_entries():
	requests.delete('https://murmuring-bastion-31969.herokuapp.com/delete')
	return redirect(url_for('index'))


if __name__=="__main__":
	app.run(debug=True)
