n=int(input("enter the number to print the next prime number"))
check=1
while(check==1):
    ct=0
    n=n+1
    for i in range(1,n+1):
        if(n%i==0):
            ct=ct+1
    if(ct==2):
        print("the next prime of that number you entered number is",n)
        check=0
        
        
