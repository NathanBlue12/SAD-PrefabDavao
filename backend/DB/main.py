import collections
from http import client
from pydoc import doc
from turtle import update
from dotenv import load_dotenv, find_dotenv 
import os
import pprint
from pymongo import MongoClient
import random
import string

load_dotenv(find_dotenv())

username = os.environ.get("dbUser_Dev") # load database connect details from local .env
password = os.environ.get("dbPass_Dev")

printer = pprint.PrettyPrinter()

print("connecting to database...") # connect to database
connectionString = f"mongodb+srv://{username}:{password}@prefabcluster.fmgvmiy.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(connectionString)

print("connecting to database ✓")

mainDB = client.main # main database
accounts_collection = mainDB.accounts 
admins_collection = mainDB.admins 
employees_collection = mainDB.employees
login_records_collection = mainDB.login_records
projects_collection = mainDB.projects
tasks_collection = mainDB.tasks


def show_mainDB_collections(): #shows collections of main DB
    collections = mainDB.list_collection_names()
    print(collections)

def create_initial_documents(): # !!!REMOVE AT DEPLOYMENT!!!
    docTemplate_account = {
        "account_username" : "testUsername",
        "account_password" : "testPassword"
    }

    docTemplate_Employee = {
        "employee_id" : "00000",
        "first_name" : "First",
        "last_name" : "Last",
        "role" : "Test Role",
        "phone_num" : "12345678901",
        "email_add" : "test@domain.com"
    }

    docTemplate_admin = {
        "admin_password" : "12345678"
    }
    
    docTemplate_project = {
        "project_id" : "11111",
        "project_name": "Poject_1",
        "project_status": "test_status_project",
        "tasks" :  ["22222"]
    }

    docTemplate_task = {
        "task_id" : "22222",
        "task_name" : "Task_1",
        "task_note" : "This is a sample task note",
        "task_status" : "test_status_task"
    }



    #accounts_collection.insert_one(docTemplate_account)
    #admins_collection.insert_one(docTemplate_admin)
    #employees_collection.insert_one(docTemplate_Employee)
    #projects_collection.insert_one(docTemplate_project)
    #tasks_collection.insert_one(docTemplate_task)

    from bson.objectid import ObjectId
    _id = ObjectId("6301f4b4f3409c133c8d62f1")
    updates = {
        "$set": {"action": "log-in"}
    }
    login_records_collection.update_one({"_id": _id}, updates)

create_initial_documents()
def get_Account_LogIn_Details(username): #gets account details
    account_details = []
    found_details = accounts_collection.find_one({"account_username": username})
    #printer.pprint(found_details)

    if found_details == None:
        print("Error Code: e0101db; Username Not Found")
        return "e0101db"
    else:
        found_id = accounts_collection.find_one({"account_username": username}, {"account_id": 1, "_id" : 0})
        account_id = found_id['account_id']
        account_details.append(account_id)

        found_username = accounts_collection.find_one({"account_username": username}, {"account_username": 1, "_id" : 0})
        account_username = found_username['account_username']
        account_details.append(account_username)

        found_password = accounts_collection.find_one({"account_username": username}, {"account_password": 1, "_id" : 0})
        account_password = found_password['account_password']
        account_details.append(account_password)
 
        return account_details

def update_Time_In(account_id, date, time):
    
    id = string.digits
    generatedID =  ''.join(random.choice(id) for i in range(5)) 
    doc_login = {
        "log_id": generatedID,
        "account_id": account_id,
        "login_date": date,
        "login_time": time,
        "action" : "log-in"
    }
    login_records_collection.insert_one(doc_login)

def update_Time_Out(account_id, date, time):
        
    id = string.digits
    generatedID =  ''.join(random.choice(id) for i in range(5)) 
    doc_logout = {
        "log_id": generatedID,
        "account_id": account_id,
        "logout_date": date,
        "logout_time": time,
        "action" : "log-out"
    }
    login_records_collection.insert_one(doc_logout)


update_Time_Out("55555", "2022-08-21", "01:59:00")
#get_Account_LogIn_Details("testUsername")
#create_initial_documents()