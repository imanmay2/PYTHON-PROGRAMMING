n=int(input("enter the number"))
b=n
ct=0
s=0
while(n!=0):
    n=n//10
    ct=ct+1
while(b!=0):
    r=b%10
    b=b//10
    if(r==1 or r==ct):
        s=s+r
print("the sum of the last and first number is",s)
