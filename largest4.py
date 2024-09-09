a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
d=int(input("d = "))
if(a>=b and a>=c and a>=d):
    print(" largest number = ",a)
elif(b>=c and b>=d):
    print("Largest number = ",b)
elif(c>d):
    print("Largest number = ",c)
else:
    print("Largest number = ",d)