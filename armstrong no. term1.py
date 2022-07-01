#armstrong number or not...
n=int(input("enter the number"))
a=n
s=0
while(a!=0):
    r=a%10
    s+=(r**3)
    a=a//10
if(s==n):
    print("armstrong number")
else:
    print("not an armstrong number")
