from datetime import date
from datetime import time
from database import databaseFuncs



class AuthSys ():

    def login(username, password):
        databaseFuncs.get_Account_LogIn_Details(username)

        #if usr == docTemplate_account and pwd == 'account_password '
        

AuthSys.login("testUsername", "Test")

         



    