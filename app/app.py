from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv(MONGO_URI), tlsCAFile=certifi.where())
db = client[os.getenv(DATABASE)]

try:
    collections = db.list_collection_names()
    print(collections)
except Exception as e:
    print(f"An error occurred: {e}")



