from database import database
from datetime import date
from datetime import datetime




class AuthSys():
    # Checker
    global date, time
    #Time
    now = datetime.now()
    #Date
    today = date.today()
    # Textual month, day and year	
    date = today.strftime("%Y-%m-%d")
    # Current Time
    time = now.strftime("%H:%M:%S")
    

    def login (username, password):
            #Find The Data inside the Collection
        global userdetails
        userdetails = database.get_Account_LogIn_Details(username=username)
    
        #userdetails 0 , 1 , 2 id , name , pass
        
        #Returns True or False Verification Process
        databaseusr = userdetails[1] #Username Database
        databasepwr = userdetails[2] #password Database
        usr = username
        pwr = password

        

        try:
            if userdetails != "e0101db":
                try:
                    #username
                    
                    if usr == databaseusr:
                        #print("Found Username")
                        try:
                            #password
                            if pwr == databasepwr:
                                        #print("Found Password")
                                        return True
                                        
                        except:
                            
                            return False
                    else:
                        return False
                except:
                    return False
            
            else:
                return "NOT FOUND"
        except:
            return False


    def LoggedIn (Verified):
        
        AuthSys.LoggedIn(Verified= AuthSys.login(username= username,password= password))
    #Find The Data inside the Collection
        if Verified == True:
        #userdetails 0 , 1 , 2 id , name , pass
            database.update_Time_In(account_id= userdetails[0], date=date, time=time )
            return True

    def LoggedOut():
        if " " == False:
            database.update_Time_Out(account_id= userdetails[0], date=date, time=time )
        else:
            print("Still Logged on")

    






#Username input Remove Later
username = input("Username: ")
password = input("Password: ")
AuthSys.login(username=username, password=password)
AuthSys.LoggedIn(Verified= AuthSys.login(username= username,password= password))
