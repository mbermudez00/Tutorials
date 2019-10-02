# mongo.py
from flask import Flask, jsonify, request 
from pymongo import MongoClient
import configparser
from bson.json_util import dumps


CONFIG_SYS = configparser.ConfigParser()
CONFIG_SYS.read("config/config.ini")

app = Flask(__name__)
title = "Flask and MongoDB"
heading = "Mau"

client = MongoClient(CONFIG_SYS["mongo"]["connect"]) #host url
db = client.MauDatabase    #Select the database
logss = db.Logss #Select the collection name

@app.route("/", methods = ['GET'])
def index():
    try:
        results = []
        for x in logss.find():
            results.append({'name': x['name'], 'age': x['age']})
        return jsonify(results)
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))

@app.route('/add', methods=['GET','POST'])
def add():
    try:
        name = request.json['name'].capitalize()
        age = int(request.json['age'])
        if name and age:
            logss.insert_one({"name":name, "age":age})
            return jsonify(message="Success!!")
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))

#@app.route("/show", methods=['GET'])
if __name__ == '__main__':
    app.run(debug=True)
 