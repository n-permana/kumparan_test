from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/kumparan_test"
app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app)
news_collection = mongo.db.news

from blog import main