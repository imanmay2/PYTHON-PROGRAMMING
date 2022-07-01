n=int(input("enter the number"))
s=0
p=n
q=n
c=0
while(p!=0):
    p=p//10
    c=c+1
while(q!=0):
    r=q%10
    s=s+r**c
    c=c-1
    q=q//10
if(s==n):
    print("diasarium number")
else:
    print("not diasarium number")
