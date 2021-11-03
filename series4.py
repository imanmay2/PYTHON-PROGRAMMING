n=int(input("enter the range of the series"))
p=1
q=2
for j in range(1,n+1):
    o=p,"/",q
    p=p+2
    q=q+2
    print(o)
    
