from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3

# this.state.propData = { // this.props.data from API
#       "Name": "Bone Marrow Transplant",
#       "Hospitals": {
#         "Sutter": 2000000,
#         "UCSF": 130000,
#         "Stanford": 300000,
#         "El Camino": 183950,
#         "West Valley": 883891
#       }
#     };




conn = sqlite3.connect(r"./data/_modified/drg.db")
conn.text_factory = str
c = conn.cursor()

c.execute("SELECT name, drg, avg_charge FROM 'master' WHERE drg = '3';")

toDict = {}
toDict['Name'] = '3'
toDict['Hospitals'] = {}

for row in c:
    toDict['Hospitals'][row[0]] = row[2]

print(toDict)
    