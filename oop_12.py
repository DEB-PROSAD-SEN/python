class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def persentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
stu1=Student(98,67,76)
print(stu1.persentage)
stu1.phy=67
print(stu1.persentage)

