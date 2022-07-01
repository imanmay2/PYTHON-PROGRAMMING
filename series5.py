n=int(input("enter the range"))
a=int(input("enter the number"))
f=1
s=0
p=1
r=0
for i in range(1,n+1):
    for j in range(1,p+1):
        f=f*j
    p=p+1   
    print(a**r,"/",f)
    o=a**r/f
    s=s+o
    f=1
    r=r+1
print("sum of the series printed above is",s)
