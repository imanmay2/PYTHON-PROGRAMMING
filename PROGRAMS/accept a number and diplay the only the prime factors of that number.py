n=int(input("enter the number to show the factors "))
print("the prime factors of the number is.......")
for i in range(1,n+1):
    if(n%i==0):
        ct=0
        for k in range(1,i+1):
            if(i%k==0):
                ct=ct+1
        if(ct==2):
            print(i)
