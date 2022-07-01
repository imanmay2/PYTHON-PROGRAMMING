x=int(input("enter the number"))
y=int(input("enter the second number"))
lcm=0
if(x>y):
    lcm=x
else:
    lcm=y
while(1):
    if(lcm%x==0 and lcm%y==0):
        break
    else:
        lcm=lcm+1
hcf=(x*y)/lcm
print("lcm is",lcm)
print("hcf is",hcf)
