k=[1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
print("Enter the number you want to search : ")
p=int(input())
idx=0
while idx<len(k):
    if(k[idx]== p):
        print("found the number ",p," at index ",idx)
    else:
        print("Not found")
    idx+=1

