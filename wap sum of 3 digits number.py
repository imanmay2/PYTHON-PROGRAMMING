num=int(input("enter"))
s=0
while(num!=0):
    r=num%10
    s=s+r
    num//=10
print("sum of digits is",s)
