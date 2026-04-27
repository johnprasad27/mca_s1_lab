import pymongo

# connect to MongoDB
conn = pymongo.MongoClient("mongodb://localhost:27017/")

# select database
db = conn['college']

# select collection
col = db['studlist']

# query
for i in col.find({"gender": "female"}):
    print(i)