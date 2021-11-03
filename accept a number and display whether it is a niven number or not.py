n=int(input("enter the number"))
a=n
s=0
while(a!=0):
    r=a%10
    s=s+r
    a=a//10
if(n%s==0):
    print(n,"is a niven number")
else:
    print(n,"is not a niven number")
