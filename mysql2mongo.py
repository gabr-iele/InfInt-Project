import mysql.connector
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client.newDB
collection = db.newCollection

conn = mysql.connector.connect(user="USERNAME", password="PASSWORD", database='InfIntDB')

cur = conn.cursor(buffered=True)

query = ("SELECT *"
         "FROM unescoviews")
cur.execute(query)

cid = 0
for (name, danger, lon, lat, category, country, relevance) in cur:
    # print(name,",",danger,",",lon,",",lat,",",category,",",country,",",relevance)
    cus = dict()
    cid += 1

    cus['_id'] = cid
    cus['name'] = name
    cus['danger'] = danger
    cus['category'] = category
    cus['country'] = country
    cus['relevance'] = relevance
    location = dict()
    location['type'] = "Point"
    location['coordinates'] = [lon, lat]
    cus['location'] = location
    collection.insert_one(cus)
