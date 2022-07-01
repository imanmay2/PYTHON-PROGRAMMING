a=float(input("enter the side"))
b=float(input("enter the side"))
c=float(input("enter the side"))
if(a+b>c or b+c>a or a+c>b):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    if(a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 ):
        print("triangle formed is right angles triangle")
        print("area is",area)
    else:
        print("it is not a right angled triangle")
        print("area of this triangle is",area)
else:
    print("it is not forming any kind of triangle hence no area")
    
        
