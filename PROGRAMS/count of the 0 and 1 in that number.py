n=int(input("enter the number"))
ct=0
n1=n
c=0
while(n!=0):
    r=n%10
    if(r==0):
        ct=ct+1
    n=n//10
while(n1!=0):
    rem=n1%10
    if(rem==1):
        c=c+1
    n1=n1//10
print("the count of the 0  is",ct)

print("the count of the 1 is",c)
