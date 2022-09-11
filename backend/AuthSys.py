from datetime import date
from datetime import time
from database import database
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://prefabdev:prefab9269@prefabcluster.fmgvmiy.mongodb.net/test")
db = cluster["main"]
collection = db["accounts"]





def get_Account_LogIn_Details(account):



#Find The Data inside the Collection
    account = collection.find_one({"account_username": usr})
    password = collection.find_one({"account_password": pwr})

    print(account)
    
    try:
        #username
        if account != None:
            print("Found Username")
            try:
                #password
                if password != None:
                            print("Found Password")
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



usr = input("Username: ")
pwr = input("Password: ")


get_Account_LogIn_Details(usr)

found_details = get_Account_LogIn_Details(usr)



#Testing if True
if found_details == True:
    print("Yatta")
else:
    print("Ōno")    

    








#Insert Data Testing Phase Remove after deployment
def Input():
    post = {"account_username": "rian", "account_password": "goodbye", "employee_id": 22222, "account_id": 22222}
    collection.insert_one(post)
    print("Success")



















    #db = client("Database")
    #if usr == docTemplate_account and pwd == 'account_password '


