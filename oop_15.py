class Circle:
    def __init__(self,red):
        self.red=red
    def area(self):
        area=3.1416*self.red*self.red
        print(area)
c1=Circle(5)
c1.area()