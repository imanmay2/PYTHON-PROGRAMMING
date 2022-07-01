n=int(input("enter the number of the range"))
num=0
prime=0
while(num<n):
    num=num+1
    ct=0
    for i in range(1,num+1):
        if(num%i==0):
            ct=ct+1
    if(ct==2):
        print(num,end=' ')
        prime=prime+1
print("the count of the previous prime numbers are",prime)

    
