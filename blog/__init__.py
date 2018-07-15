from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/kumparan_test"
mongo = PyMongo(app)
news_collection = mongo.db.news

from blog import main