ct=0
l=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,8,8,8,8,8]
n=int(input("enter the number"))
for i in l:
    if(i==n):
        ct=ct+1
print(ct)
