x=int(input("enter the number"))
n=int(input("enter the range of the series"))
s=0
f=1
for i in range(1,n+1):
    i=i-1
    f=f*i
    s+=(x**i)/f
print("the sum of the series is",s)
