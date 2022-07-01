n=int(input("enter the number"))
a=n
ct=0
while(a!=0):
    r=a%10
    ct=ct+1
    a=a//10
if(ct==7):
    f=n%10
    l=(n//1000000)%10
    s=f+l
    print("the sum of the last and the first digit is",s)
else:
    print("not a 7 digit number")
