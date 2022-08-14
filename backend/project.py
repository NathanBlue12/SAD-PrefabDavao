from aifc import Error
#from employee import Employee
from task import Task

class Project:
    def __init__(self, projectID, projectStatus, employee, task, projectCompleted = False):
        self.projectID = projectID
        self.projectStatus = projectStatus
        self.projectCompleted = projectCompleted
        self.employees = [] 
        self.tasks = []
   
    def add_task(self, task): #adds task to project
            if not isinstance(task, Task):
                raise Error("Invalid Task...")    
            self.tasks.append(task)   


    def projectStatusGive(self): #gives that status of the project
        return self.projectStatus     