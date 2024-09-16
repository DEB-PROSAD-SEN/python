class Employ:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showdata(self):
        print(self.role)
        print(self.department)
        print(self.salary)
c=Employ("teacher","ece",50000)
c.showdata()