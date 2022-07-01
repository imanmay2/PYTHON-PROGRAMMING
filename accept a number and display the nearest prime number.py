n=int(input("enter the number to print the nearest prime number"))
a=n
m=a
while(1):
    ct=0
    a=a+1
    for i in range(1,a+1):
        if(a%i==0):
            ct=ct+1
    if(ct==2):
        break
while(1):
    ct=0
    m=m-1
    for i in range(1,m+1):
        if(m%i==0):
            ct=ct+1
    if(ct==2):
        break
if((a-n)<(n-m)):
    print("the nearest prime number is",a)
elif((n-m)<(a-n)):
    print("the nearest prime number is",m)
else:
    print("the nearest prime number is both",a,m)
