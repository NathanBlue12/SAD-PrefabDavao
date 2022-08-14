from employee import Employee

class Admin(Employee):
    def __init__(self, employeeID, firstName, lastName, role, phoneNum, email, salary, account, adminPass):
        super().__init__(self, employeeID, firstName, lastName, role, phoneNum, email, salary, account)
        self.adminPass = adminPass

    def hasFullPerms(self):
        return False

s1 = Admin(00000, "Therone", "Almadin", "Admin", "000000", "therone@gmail.com", "0000", "0000", "0000")

print(Admin.hasFullPerms(s1))