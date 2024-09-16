class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")
    def __add__(self,c1):
        newreal=self.real+c1.real
        newimg =self.imaginary+c1.imaginary
        return Complex(newreal,newimg)
    def __sub__(self,c1):
        newreal=self.real-c1.real
        newimg =self.imaginary-c1.imaginary
        return Complex(newreal,newimg)
    def __mul____(self,c1):
        newreal=self.real*c1.real
        newimg =self.imaginary*c1.imaginary
        return Complex(newreal,newimg)
    def __truediv____(self,c1):
        newreal=self.real/c1.real
        newimg =self.imaginary/c1.imaginary
        return Complex(newreal,newimg)
    # Adding the __str__ method to represent the object as a string
    #def __str__(self):
        #return f"{self.real}i + {self.imaginary}j"
c1 = Complex(1,3)
c1.shownumber()
c2=Complex(4,6)
c2.shownumber() 
c3=c1+c2
c3.shownumber()
c4=c1-c2
c4.shownumber() 