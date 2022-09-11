from pymongo import MongoClient
from database import database
from datetime import date
from datetime import datetime

# datetime object containing current date and time
#Time
now = datetime.now()
#Date
today = date.today()


cluster = MongoClient("mongodb+srv://prefabdev:prefab9269@prefabcluster.fmgvmiy.mongodb.net/test")
client = cluster

mainDB = client.main 

accounts_collection = mainDB.accounts 
admins_collection = mainDB.admins 
employees_collection = mainDB.employees
log_records_collection = mainDB.log_records
projects_collection = mainDB.projects
tasks_collection = mainDB.tasks

db = cluster["main"]
collection = db["accounts"]




# Checker
def Authorization (username):

#Find The Data inside the Collection
    usr = accounts_collection.find_one({"account_username": username})
    pwr = accounts_collection.find_one({"account_password": password})

    #print(pwr)
    
    
    try:
        #username
        if usr != None:
            #print("Found Username")
            try:
                #password
                if pwr != None:
                            #print("Found Password")
                            return True
                            
            except:
                print("Password not found")
                return False
        else:
            print("Username not found")
            return False
    except:
        print("No Data")
        return False


#Find ID
def account_id(username):
        found_id = accounts_collection.find_one({"account_username": username}, {"account_id": 1, "_id" : 0})
        account_id = found_id['account_id']
        return account_id



    # Textual month, day and year	
date = today.strftime("%Y %B, %d")
#print("d2 =", date)
# Current Time
time = now.strftime("%H:%M")
#print("time =", time)	



#Username input Remove Later
username = input("Username: ")
password = input("Password: ")


#Verification Process
Authorization(username)

#Returns True or False
Verified = Authorization(username)

#Once Finish Verifying pass to get Account login details


#Testing if True
if Verified == True:
    #print("Yatta")
    account_id(username= username)
    database.get_Account_LogIn_Details(username= username)
    #print(database.get_Account_LogIn_Details(username= username))
    database.update_Time_In(account_id= account_id(username=username), date=date, time=time )
    
else:
    print("Ōno")    
















