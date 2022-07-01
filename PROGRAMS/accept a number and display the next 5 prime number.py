n=int(input("enter the number"))
p=0
while(p<5):
    ct=0
    n=n+1
    for i in range(1,n+1):
        if(n%i==0):
            ct=ct+1
    if(ct==2):
        print(n,end=' ')
        p=p+1
        
