mark=int(input("Enter your mark : "))
if(mark>=90):
    print("A")
elif(mark<90 and mark>=80):
    print("B")
elif(mark<80 and mark >= 70):
    print("C")
elif(mark<70 and mark>=60):
    print("D")
else:
    print("Fail")