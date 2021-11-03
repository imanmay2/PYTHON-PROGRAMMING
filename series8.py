p=0
r=3
n=int(input("enter the range of the series"))
for i in range(1,n+1):
    print(p,end=' ')
    p=p+r
    r=r+2
