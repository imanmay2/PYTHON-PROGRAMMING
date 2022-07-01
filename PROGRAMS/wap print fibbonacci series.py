a=0
b=1
n=int(input("enter the range of the series"))
for i in range(3,n+1):
    print(a,b,end=' ')
    c=a+b
    a=b
    b=c
    
