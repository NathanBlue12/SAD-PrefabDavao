from employee import Employee

class Admin(Employee):
    def __init__(self, employeeID, firstName, lastName, role, phoneNum, email, salary, account, adminPass):
        super().__init__(self, employeeID, firstName, lastName, role, phoneNum, email, salary, account)
        self.adminPass = adminPass

    def hasFullPerms(self):
        return True

