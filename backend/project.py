from aifc import Error
from employee import Employee
from task import Task

class Project:
    def __init__(self, projectID, projectStatus, employee, task, projectCompleted = False):
        self.projectID = projectID
        self.projectStatus = projectStatus
        self.projectCompleted = projectCompleted
        self.employees = [] 
        self.tasks = []

        if isinstance(employee, Employee):
            self.employees.append(employee)
        elif isinstance (employee, list):
            for entry in employee:
                if not isinstance(entry, Employee):
                    raise Error("Invalid Employee...")

            self.employees = employee
        else:
            raise Error("Invalid Employee...")        

    def add_employee (self, employee): #assigns project to an employee
        if not isinstance (employee, Employee):
            raise Error ("Invalid Employee...")
        self.employees.append(employee)
    
    def add_task(self, task): #adds task to project
            if not isinstance(task, Task):
                raise Error("Invalid Task...")    
            self.tasks.append(task)   


    def projectStatusGive(self): #gives that status of the project
        return self.projectStatus     