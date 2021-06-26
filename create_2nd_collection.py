import mysql.connector
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client.BDM
collection = db.GroupedSites

username = ""
password = ""

credentials = f.readlines()
conn = mysql.connector.connect(user=username, password=password, database="InfIntDB")
cur = conn.cursor(buffered=True)

query_1 = ("SELECT lon, lat FROM geoviews WHERE category='Amphitheater'")
query_2 = ("SELECT lon, lat FROM geoviews WHERE category='Amphitheater' and country='Spain'")


cur.execute(query_1)

cus = dict()
cus['_id'] = 1
cus['description'] = "All amphitheaters"
points = dict()
points['type'] = "MultiPoint"
points['coordinates'] = []

for (lon, lat) in cur:
    points['coordinates'].append([lon, lat])
cus['points'] = points
collection.insert_one(cus)

cur.execute(query_2)

cus = dict()
cus['_id'] = 2
cus['description'] = "All amphitheaters in Spain"
points = dict()
points['type'] = "MultiPoint"
points['coordinates'] = []

for (lon,lat) in cur:
    points['coordinates'].append([lon, lat])
cus['points'] = points
collection.insert_one(cus)
