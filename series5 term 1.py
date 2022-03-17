x=int(input("enter the number"))
n=int(input("enter the range of the series"))
s=0
for i in range(0,n):
    if(i%2==0):
        s+=x**i
    else:
        s-=x**i
print("the sum of the series is",s)
