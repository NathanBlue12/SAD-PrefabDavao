from database import database
from datetime import date
from datetime import datetime

# datetime object containing current date and time
#Time
now = datetime.now()
#Date
today = date.today()

# Textual month, day and year	
date = today.strftime("%Y-%m-%d")
#print("d2 =", date)
# Current Time
time = now.strftime("%H:%M:%S")
#print("time =", time)	

class AuthSys():
    # Checker
    def Authorization (user):
        
    #Find The Data inside the Collection
        
        databaseusr = userdetails[1] #Username Database
        databasepwr = userdetails[2] #password Database
        usr = user
        pwr = passw
        
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
                    print("Password not found")
                    return False
            else:
                print("Username not found")
                return False
        except:
            print("No Data")
            return False
    def LoggingIn(Verified):
        if Verified == True:
            #print("Yatta")
            #userdetails 0 , 1 , 2 id , name , pass
            database.update_Time_In(account_id= userdetails[0], date=date, time=time )
            return True
        else:
            print("Ōno")    
            
    def LoggingOut(Status):
        if Status == False:
            database.update_Time_Out(account_id= userdetails[0], date=date, time=time )
        else:
            print("Still Logged on")




#Username input Remove Later
user = input("Username: ")
passw = input("Password: ")

#userdetails 0 , 1 , 2 id , name , pass
userdetails = database.get_Account_LogIn_Details(username=user)
#Returns True or False Verification Process
Verified = AuthSys.Authorization(user= user)

AuthSys.Logging(Verified= Verified)



