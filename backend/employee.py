from aifc import Error
from account import Account
from project import Project

class Employee:
    def __init__(self, employeeID, firstName, lastName, role, phoneNum, email, salary, account, project):
        self.employeeID = employeeID
        self.firstName = firstName
        self.lastName = lastName
        self.role = role
        self.phoneNum = phoneNum
        self.email = email
        self.salary = salary
        self.account = account
        self.projects = []

        def add_project(self, project):
            if not isinstance(project, Project):
                raise Error("Invalid Project...")    
            self.projects.append(project) 
"""
        if isinstance(project, Project):
            self.projects.append(project)
        elif isinstance (project, list):
            for entry in project:
                if not isinstance(entry, Project):
                    raise Error("Invalid Project...")

            self.projects = project
        else:
            raise Error("Invalid Project...")

        def add_project(self, project):
            if not isinstance(project, Project):
               raise Error("Invalid Project...")

            self.projects.append(project)

  """      

        