# conexión
# from settings import DATABASE_MONGO
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
#Set databases
con = MongoClient('localhost',27017)
DATABASE_MONGO = con.calls

# colección
phones = DATABASE_MONGO.phones_twilio
result = phones.find_one(ObjectId("5d3760d854a6363dac3a84fb"))
bitacora = {
    "twilio_phone":"dd",
    "info": None,
    "text": "que ",
    "comments":"dd",
    "last_intent":"",
    "dangerous_flag":0
}
p = phones.insert_one(bitacora).inserted_id
print(p)