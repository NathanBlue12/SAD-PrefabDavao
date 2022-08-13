from project import Project

class Task:
    def __init__(self, taskID, taskNotes, project, status, taskCompleted = False):
        self.taskID = taskID
        self.taskNotes = taskNotes
        self.taskCompleted = taskCompleted
        self.status = status
    
    def giveStatus(self):
        return self.status

