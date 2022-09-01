from datetime import date
from datetime import datetime
import uuid 
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

datetime = date
today = date.today()





class get_Account_Login_Details ():


    def register ():

        # Textual month, day and year	
        d2 = today.strftime("%B %d, %Y")

        currentdate = d2

        print("d2 =", d2)

        # dd/mm/YY H:M:S
        
        currenttime = now.strftime(" %H:%M:%S")
        nowtime = currenttime
        print("time =", currenttime)	

        db = open ("backend\DB\Test\database.txt", "r")
        Username = input("Create username: ")
        Password = input("Create password: ")
        Password1 = input("Confirm password: ")


        d = []
        f = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        print(data)
        print("Today's date", date)

    #Password Checker and Restarter
        if Password != Password1:
            print("Passwords dont match, restart")
            register()

    #Length of Password
        else:
            if len(Password) <=6:
                print("Password too Short, restart:")
                register()

            #Check if Username Exists in Database and user cannot proceed w out using a different name    
            elif Username in d:
                print("Username exists")
                register()
            #Saves data into the database
            else:
                db = open("backend\DB\Test\database.txt", "a")
                db.write(Username+", "+Password+", "+currentdate+","+currenttime+"\n")
                print("Success!")



    
    def access ():
        db = open("backend\DB\Test\database.txt", "r")
        Username = input("Enter your username: ")
        Password = input("Enter your password: ")
        

        if not len(Username or Password)<1:

            d = []
            f = []
            for i in db:
                a,b = i.split(", ")
                b = b.strip()
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))

            try: 
                if data[Username]:
                    try:
                        if Password == data[Username]:
                            print("Login Succesful")
                            print("Hi,", Username)
                        else:
                            print("Password or Username Incorrect")
                    except:
                        print("Incorrect password")
                else:
                    print("Username or Password doesn't exist")
            except:
                print("Username or Password doesn't exist")
        else:
            print("Please Enter a Value")

    #Home 
    def home(option=None):
        option = input("Login | Signup:")
        if option == "Login":
            access()

        elif option == "Signup":
            register()

        else:
            print("Please enter an option")
    home()