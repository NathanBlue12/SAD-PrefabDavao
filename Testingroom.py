from datetime import date
from datetime import time
from operator import truediv
from pymongo import MongoClient





cluster = MongoClient("mongodb+srv://prefabdev:prefab9269@prefabcluster.fmgvmiy.mongodb.net/test")
db = cluster["main"]
collection = db["accounts"]




post = {"account_username": "nathan", "account_password": "pepega", "employee_id": 55555, "account_id": 55555}
collection.insert_one(post)
    





