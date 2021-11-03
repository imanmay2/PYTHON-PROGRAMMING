n=int(input("enter the range"))
n1=n
r=1
p=0
while(r<=n1):
    if(r%2!=0):
        for i in range(1,n+1):
            p=p+r
            print(r)
    r=r+1
