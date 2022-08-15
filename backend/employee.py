from aifc import Error
from account import Account
from project import Project

class Employee:
    def __init__(self, employeeID, firstName, lastName, role, phoneNum, email, account, project):
        self.employeeID = employeeID
        self.firstName = firstName
        self.lastName = lastName
        self.role = role
        self.phoneNum = phoneNum
        self.email = email
        self.accounts = []
        self.projects = []

        if isinstance(project, Project):
            self.projects.append(project)
        elif isinstance (project, list):
            for entry in project:
                if not isinstance(entry, Project):
                    raise Error("Invalid Project...")
            self.projects = project
        else:
            raise Error("Invalid Project...")

        if isinstance(account, Account):
            self.accounts.append(account)
        elif isinstance (account, list):
            for entry in account:
                if not isinstance(entry, Account):
                    raise Error("Invalid Account...")
            self.accounts = account
        else:
            raise Error("Invalid Account...")            

    def add_project(self, project): #adds project to an employee's load
        if not isinstance(project, Project):
                raise Error("Invalid Project...")    
        self.projects.append(project) 

    def add_account(self, account): #adds project to an employee's load
        if not isinstance(account, Account) and len(self.accounts) > 1:
                raise Error("Invalid Project...")    
        self.accounts.append(account) 
     

        