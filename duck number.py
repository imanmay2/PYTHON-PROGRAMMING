n=int(input("enter the number"))
f=0
while(n!=0):
    r=n%10
    if(r==0):
        print("a duck number")
        f=1
        break
    n=n//10
if(f==0):
    print("not a duck number")
