#wap accept a no. and reverse the number without using the modulo function.
n=int(input("enter any number you want to enter"))
s=0
while(n>0):
    x=n//10
    f=x*10
    r=n-f
    s=(s*10)+r
    n=n//10
print("the reverse no. without using the modulo one is",s)
