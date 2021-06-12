import mysql.connector
from pymongo import MongoClient


def getGeoviewsData(cur, cid, collection):
    
    queryGeo = ("SELECT * FROM geoviews")
    cur.execute(queryGeo)

    for (name, lon, lat, country, category, relevance) in cur:
            
        cus = dict()
        cid += 1

        cus['_id'] = cid
        cus['name'] = name
        cus['category'] = category
        if(country is not None):
            cus['country'] = country
        if(relevance is not None):
            cus['relevance'] = relevance
        cus['provenance'] = 'GeoNames'
        location = dict()
        location['type'] = "Point"
        location['coordinates'] = [lon, lat]
        cus['location'] = location
        collection.insert_one(cus)

    return cid

        
def getUnescoviewsData(cur, cid, collection):
    
    queryUnesco = ("SELECT * FROM unescoviews")
    cur.execute(queryUnesco)

    for (name, danger, lon, lat, category, country, relevance) in cur:
        
        cus = dict()
        cid += 1

        cus['_id'] = cid
        cus['name'] = name
        cus['danger'] = danger
        cus['category'] = category
        if(country is not None):
            cus['country'] = country
        if(relevance is not None):
            cus['relevance'] = relevance
        cus['provenance'] = 'Unesco'
        location = dict()
        location['type'] = "Point"
        location['coordinates'] = [lon, lat]
        cus['location'] = location
        collection.insert_one(cus)
        
    return cid


    
def createMongoDB(mongoClient, userSQL, passwordSQL, databaseSQL):

    client = MongoClient(mongoClient)
    db = client.bigDataManagementDB
    collection = db.bigDataManagementCollection

    conn = mysql.connector.connect(user=userSQL, password=passwordSQL, database=databaseSQL)

    cur = conn.cursor(buffered=True)

    cid = 0

    cid = getGeoviewsData(cur, cid, collection)

    cid = getUnescoviewsData(cur, cid, collection)

    print("Cid:", cid)

    


createMongoDB("mongodb://127.0.0.1:27017/", 'root', "", 'infintproject') 
