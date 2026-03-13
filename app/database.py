from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment variables from .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# create MongoDB client
client = MongoClient(MONGO_URI)

# select database
db = client[DB_NAME]

# collections
questions_collection = db["questions"]
sessions_collection = db["user_sessions"]