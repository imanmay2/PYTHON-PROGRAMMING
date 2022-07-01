n=int(input("enter the number"))
res=0
while(n!=0):
    r=n%10
    n=n//10
    res=(res*10)+r
print("reverse number is",res)
