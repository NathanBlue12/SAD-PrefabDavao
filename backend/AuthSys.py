from database import database
from datetime import date
from datetime import datetime

#Time
now = datetime.now()
#Date
today = date.today()

# Textual month, day and year	
date = today.strftime("%Y-%m-%d")
# Current Time
time = now.strftime("%H:%M:%S")


class AuthSys():
    # Checker
    global date, time
    # Textual month, day and year	
    date = today.strftime("%Y-%m-%d")
    # Current Time
    time = now.strftime("%H:%M:%S")

    def Authorization (user):
        
    #Find The Data inside the Collection
        global userdetails
        userdetails = database.get_Account_LogIn_Details(username=user)
    


        #userdetails 0 , 1 , 2 id , name , pass
        
        #Returns True or False Verification Process
        databaseusr = userdetails[1] #Username Database
        databasepwr = userdetails[2] #password Database
        usr = user
        pwr = passw

        

        try:
            if userdetails != "e0101db":
                try:
                    #username
                    
                    if usr == databaseusr:
                        print("Found Username")
                        try:
                            #password
                            if pwr == databasepwr:
                                        print("Found Password")
                                        return True
                                        
                        except:
                            print("NOT FOUND")
                            return False
                    else:
                        print("NOT FOUND")
                        return False
                except:
                    return False
            
            else:
                print("NOT FOUND")
                return False
        except:
            return False

    
    def LoggingIn(Verified):
        if Verified == True:
            #userdetails 0 , 1 , 2 id , name , pass
            database.update_Time_In(account_id= userdetails[0], date=date, time=time )
            return True
        

            
    def LoggingOut(Status):
        if Status == False:
            database.update_Time_Out(account_id= userdetails[0], date=date, time=time )
        else:
            print("Still Logged on")

    






#Username input Remove Later
user = input("Username: ")
passw = input("Password: ")
AuthSys.Authorization(user=user)
AuthSys.LoggingIn(Verified= AuthSys.Authorization(user= user))
