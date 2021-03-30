from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import sqlite3
app = Flask(__name__)
CORS(app)


# returns React search page SPA
@app.route('/', methods=['GET'])
def index():
	return json.dumps({'hello':'world'})

# searches for hospitals based on procedure, location, radius
@app.route('/search/', methods=['POST'])
def search():
	data = request.get_json()
	print('data', data)

	conn = sqlite3.connect(r"./data/_modified/drg.db")
	conn.text_factory = str
	c = conn.cursor()
	try:
		c.execute("SELECT name, drg, description, AverageCoveredCharges FROM 'master' WHERE (upper(description) LIKE '%"+ data['procedure'] + "%' or drg LIKE '%"+ data['procedure'] + "%')AND (upper(description) NOT LIKE '%WITHOUT MCC%');")

		#c.execute("SELECT name, drg, avg_charge FROM 'master' WHERE drg = '"+ data['procedure'] +"';")

		toDict = {}
		toDict['Hospitals'] = {}

		first = True
		for row in c:
			price = row[3]
			if int(price) < 1:
				continue
			if first:
				toDict['Name'] = str(row[2])
				toDict['DRG'] = str(row[1])
				first = False
			toDict['Hospitals'][row[0]] = row[3]
	except sqlite3.OperationalError as e:
			print("sqlite error: " + e.args[0])  # table companies already exists
	# data.procedure = search bar contents (drg or keyword of desc), data.location, data.radius
	
	return json.dumps(toDict)
	#pass # use data to write SQL queries, collate into json, and return

# autocompletes procedure name based on what's typed in so far
@app.route('/autocomplete/<typed>', methods=['GET'])
def autocomplete(typed):
	pass
