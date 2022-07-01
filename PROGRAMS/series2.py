n=int(input("enter the range of the series"))
p=0
r=1
print("the required series is")
for i in range(1,n+1):
    p=p+r
    r=r+2
    print(p)
