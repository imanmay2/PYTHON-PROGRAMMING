n=int(input("enter the number"))
c=0
while(c==0):
    ct=0
    n=n+1
    for i in range(1,n+1):
        if(n%i==0):
            ct=ct+1
    if(ct==2):
        c=1
print(n)

        
