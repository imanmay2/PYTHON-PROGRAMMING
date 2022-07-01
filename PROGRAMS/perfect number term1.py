# perfect number or not....
n=int(input("enter the number"))
s=0
for i in range(1,n):
    if(n%i==0):
        s+=i
if(s==n):
    print("perfect number")
else:
    print("not a perfect number")
