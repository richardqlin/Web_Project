from flask import Blueprint,request

from database import Database

import json

api=Blueprint('api', __name__,template_folder='templates')

@api.route('/entries')

def get_all_entries():
	entries=Database.get_records()
	for entry in entries:
		entry['_id']=str(entry['_id'])
	return json.dumps(entries)


@api.route('/delete', methods=['DELETE'])

def delete_all_entries():
	Database.delete_all_records()
	return 'Record successfully deleted!'


@api.route('/post',methods=['POST'])

def add_entry():
	doc={
	'title':request.form['title'],
	'post':request.form['post']
	}

	Database.insert_record(doc)
	return 'Record successfully added'