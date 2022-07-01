n=int(input("enter the range of the series"))
s=0
p=1
r=1
q=1
for i in range(1,n+1):
    s=s+(p/q)
    o=p,'/',q
    p=p+2
    r=r+2
    q=q+r
    print(o)
print("the sum of the series is",s)
