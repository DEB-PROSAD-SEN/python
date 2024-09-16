class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def wellcome(self):
        print("Welcome student")
    def getmarks(self):
        return self.marks
    def givemark(self):
        x=int(input())
        print(x)
s1=student("Deb",98)
s1.wellcome()
print(s1.getmarks())
s1.givemark()