n=int(input("enter the number"))
ct=0
while(n!=0):
    r=n%10
    if(r%2==0):
        ct=ct+1
    n=n//10
print("the count of the even digits is",ct)
    
