n=int(input("enter the number"))
ct=0
prime=0
while(1):
    for i in range(1,n+1):
        if(n%i==0):
            ct=ct+1
    if(i==n):
        break
    elif(ct==2):
        prime=prime+1
print("the count of the prime number is",prime)
        

    
