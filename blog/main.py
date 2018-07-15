from flask import request
from blog import app, news_collection
import json
from bson import json_util, ObjectId

@app.route("/")
@app.route("/home")
def home():
    return """Test Kumparan"""

@app.route("/news", methods=['GET'])
def get_news():
    filter_status = request.args.get('status')
    filter_topic = request.args.get('topic')
    if filter_status == None:
      filter_status = ""
    if filter_topic == None:
      filter_topic = ""
    news_list = json_util.dumps(news_collection.find({'status':{"$regex": filter_status},'topics':{"$regex": filter_topic}}))
    return news_list

@app.route("/news/<id>", methods=['GET'])
def get_news_by_id(id):
    news = json_util.dumps(news_collection.find_one({'_id':ObjectId(id)}))
    return news


@app.route("/news/<id>", methods=['DELETE'])
def remove_news_by_id(id):
    data = {"status":"deleted"}
    print(json_util.dumps(news_collection.find({'_id':ObjectId(id)})))
    news_collection.update_one({'_id':ObjectId(id)}, {"$set": data}, upsert=False)
    return response_format({"success":True,"message":"News sucessfully deleted"})

@app.route("/news", methods=['POST'])
def create_news():
    news = json.loads(request.data)
    if 'title' not in news:
      return response_format({"success":False,"message":"title is required"})
    if 'content' not in news:
      return response_format({"success":False,"message":"content is required"})
    if 'status' not in news:
        news['status'] = 'draft'
    inserted_id = news_collection.insert_one(news).inserted_id
    return response_format({"success":True,"message":""})

def response_format(message):
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response
