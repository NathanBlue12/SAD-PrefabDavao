from datetime import date
from datetime import time
from database import database



class AuthSys ():

    def login(username, password):
        database.get_Account_LogIn_Details(username)

        #if usr == docTemplate_account and pwd == 'account_password '
        

AuthSys.login("testUsername", "Test")

         



    