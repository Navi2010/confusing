class employee:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def x(self):
        print(self.name)
        print(self.idnumber)

class intern(employee):
    def __init__(self, name, idnumber, position, salary):
        self.position = position
        self.salary = salary
        employee.__init__(self, name, idnumber)
    def y(self):
        print(self.position)
        print(self.salary)

ob1 = intern('navya', 942366, 'student', '$0')
ob1.x()
ob1.y()