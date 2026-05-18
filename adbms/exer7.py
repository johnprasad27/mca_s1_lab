import pymongo
import json

conn = pymongo.MongoClient("mongodb://localhost:27017/")

db = conn['college']
col = db['studlist']

with open("students.json") as file:
    data = json.load(file)

col.insert_many(data)

print("Data inserted successfully")