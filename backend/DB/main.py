import collections
from http import client
from dotenv import load_dotenv, find_dotenv 
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv()) 

username = os.environ.get("dbUser_Dev") # load database connect details from local .env
password = os.environ.get("dbPass_Dev")

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
 pass
