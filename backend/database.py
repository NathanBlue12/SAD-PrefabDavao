import collections
from pydoc import doc
from turtle import update
from dotenv import load_dotenv, find_dotenv 
import os
import pprint
from pymongo import MongoClient
import random
import string
from http import client

load_dotenv(find_dotenv())

username = os.environ.get("dbUser_Dev") # load database connect details from local .env
password = os.environ.get("dbPass_Dev")

printer = pprint.PrettyPrinter()

print("connecting to database...") # connect to database

try:
    connectionString = f"mongodb+srv://{username}:{password}@prefabcluster.fmgvmiy.mongodb.net/?retryWrites=true&w=majority" 
    client = MongoClient(connectionString)
except:
    print("Error Code: e0301")

print("connecting to database ✓")

mainDB = client.main 
accounts_collection = mainDB.accounts 
admins_collection = mainDB.admins 
employees_collection = mainDB.employees
log_records_collection = mainDB.log_records
projects_collection = mainDB.projects
tasks_collection = mainDB.tasks

class database():

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
        _id = ObjectId("6301399196ea90a251c7936b")
        updates = {
            "$set": {"projects": []}
        }
        employees_collection.update_one({"_id": _id}, updates)
        
    def testingPrint():
        print("TEST")
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
    print(get_Account_LogIn_Details("testUsername"))
    def update_Time_In(account_id, date, time): #pushes new time in details in database
        
        id = string.digits
        generatedID =  ''.join(random.choice(id) for i in range(5)) 
        doc_login = {
            "log_id": generatedID,
            "account_id": account_id,
            "login_date": date,
            "login_time": time,
            "action" : "log-in"
        }
        log_records_collection.insert_one(doc_login)

    def update_Time_Out(account_id, date, time): #pushes new time out details in database
            
        id = string.digits
        generatedID =  ''.join(random.choice(id) for i in range(5)) 
        doc_logout = {
            "log_id": generatedID,
            "account_id": account_id,
            "logout_date": date,
            "logout_time": time,
            "action" : "log-out"
        }
        log_records_collection.insert_one(doc_logout)

    def add_employee_projects(employee_id, project_id):#adds projects in employee
        
        found_project_container = employees_collection.find_one({"employee_id": employee_id}, {"projects": 1, "_id" : 0})
        project_container = found_project_container['projects']
        project_container.append(project_id)
        update = {
            "$set": {"projects": project_container}
        }
        employees_collection.update_one({"employee_id": employee_id}, update)
        printer.pprint(project_container)

    def get_employee_projects (employee_id): #gets employee's involved projects
        found_project_container = employees_collection.find_one({"employee_id": employee_id})
        project_container = found_project_container['projects']
        
        return project_container

    def admin_Checking (employee_id):#checkes whether an employee is an admin
        
        found_admin = employees_collection.find_one({"employee_id": employee_id}, {"is_Admin" : 1, "_id":0})

        if found_admin == None:
            print("Error Code: e0201db; Employee ID Not Found")
            return "e0201db"
        else:
            admin = found_admin['is_Admin']
            return admin

    def create_Project(projectName): #creates new project
        id = string.digits
        generatedID =  ''.join(random.choice(id) for i in range(5)) 

        Template_project = {
            "project_id" : generatedID,
            "project_name": projectName,
            "project_status": "None",
            "tasks" :  []
        }

        projects_collection.insert_one(Template_project)

    def delete_Project(project_id): # deletes project
        
        found_project = projects_collection.find_one({"project_id": project_id}, {"project_id": 1, "_id" : 0})

        if found_project == None:
            print ("Erorr Code: e0401 project not found")
            return "e0401"
        else:
            projects_collection.delete_one({"project_id": project_id})

    def get_Project_Details(project_id): #gets project details from project ID
        project_Details = []
        found_Project = projects_collection.find_one({"project_id": project_id})

        if found_Project == None:
            print("Error Code: e0102db; Project ID  Not Found")
            return "e0102db"
        else:
            found_id = projects_collection.find_one({"project_id": project_id}, {"project_id": 1, "_id" : 0})
            project_id = found_id['project_id']
            project_Details.append(project_id)
            
            found_name = projects_collection.find_one({"project_id": project_id}, {"project_name": 1, "_id" : 0})
            project_name = found_name['project_name']
            project_Details.append(project_name) 

            found_status = projects_collection.find_one({"project_id": project_id}, {"project_status": 1, "_id" : 0})
            project_status = found_status['project_status']
            project_Details.append(project_status) 

            found_tasks = projects_collection.find_one({"project_id": project_id}, {"tasks": 1, "_id" : 0})
            tasks = found_tasks['tasks']
            project_Details.append(tasks) 

            return project_Details
    
    def create_Task(task_name, project_id): #creates task and assigns it to project
        id = string.digits
        generatedID =  ''.join(random.choice(id) for i in range(5)) 

        Template_task = {
            "task_id" : generatedID,
            "task_name": task_name,
            "task_note": "None",
            "task_status" :  "None",
            "project_assigned_to": project_id
        }

        tasks_collection.insert_one(Template_task)  

        found_task_container = projects_collection.find_one({"project_id": project_id}, {"tasks": 1, "_id" : 0})
        task_container = found_task_container['tasks']
        task_container.append(generatedID)

    def delete_Task(task_id): #deletes task and id from task container in project   
        found_task = tasks_collection.find_one({"task_id": task_id}, {"task_id": 1, "_id" : 0})

        if found_task == None:
            print ("Erorr Code: e0402 task not found")
            return "e0402"
        else:
            found_project_id = tasks_collection.find_one({"task_id": task_id}, {"project_assigned_to": 1, "_id" : 0})
            project_id = found_project_id['project_assigned_to'] 

            tasks_collection.delete_one({"task_id": task_id})

            found_task_container = projects_collection.find_one({"project_id": project_id}, {"tasks": 1, "_id" : 0})
            task_container = found_task_container['tasks']
            task_container.remove(task_id)

            update = {
            "$set": {"tasks": task_container}
            }

            projects_collection.update_one({"project_id": project_id}, update)

    def get_Task_Details(task_id):
        task_Details = []
        found_Task = tasks_collection.find_one({"task_id": task_id})

        if found_Task == None:
            print("Error Code: e0103db; Task Not Found")
            return "e0103db"
        else:
            found_id = tasks_collection.find_one({"task_id": task_id}, {"task_id": 1, "_id" : 0})
            task_id = found_id['task_id']
            task_Details.append(task_id)
            
            found_name = tasks_collection.find_one({"task_id": task_id}, {"task_name": 1, "_id" : 0})
            task_name = found_name['task_name']
            task_Details.append(task_name) 

            found_note = tasks_collection.find_one({"task_id": task_id}, {"task_note": 1, "_id" : 0})
            task_note = found_note['task_note']
            task_Details.append(task_note) 

            found_status = tasks_collection.find_one({"task_id": task_id}, {"task_status": 1, "_id" : 0})
            task_status = found_status['task_status']
            task_Details.append(task_status) 

            return task_Details

    #print(get_Task_Details("22222"))