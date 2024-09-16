class Employ:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showdata(self):
        print(self.role)
        print(self.department)
        print(self.salary)  
class Engineer(Employ):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","70000")
    def showdata(self):
        print("Name:", self.name)
        print("Age:", self.age)
        # Call the parent class showdata() to show the role, department, and salary
        super().showdata()
c1=Engineer("DEb",25)
c1.showdata()