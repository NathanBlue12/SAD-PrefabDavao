#from project import Project

class Task:
    def __init__(self, taskID, taskNotes, status, taskCompleted = False):
        self.taskID = taskID
        self.taskNotes = taskNotes
        self.taskCompleted = taskCompleted
        self.status = status    
    
    def giveStatus(self): #gives status of task
        return self.status

s1 = Task(000000, "Nothing", "COMPLETED", True)

print(Task.giveStatus(s1))