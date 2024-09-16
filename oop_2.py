class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in Database..")
s1 = Student("DEB",87)
print(s1.name,s1.marks)