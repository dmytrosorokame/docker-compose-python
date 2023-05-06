from pymongo import MongoClient
from pprint import pprint


MONGO_URI = "mongodb://mongo:27017"
client = MongoClient(MONGO_URI)
db = client.admin
db_list = db.command("listDatabases")
pprint(db_list)