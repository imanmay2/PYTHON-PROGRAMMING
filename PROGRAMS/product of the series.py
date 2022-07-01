n=int(input("enter the range"))
r=1
p=1
for i in range(1,n+1):
    print(r)
    p=p*r
    r=r+0.2
print("the product of the series is",p)
