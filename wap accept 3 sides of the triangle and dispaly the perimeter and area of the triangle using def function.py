def area():
    per=a+b+c
    s=per/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("the perimeter of the triangle is",per)
    print("the area of the triangle is",area)
a=float(input("enter the side of the triangle"))
b=float(input("enter the side of the triangle"))
c=float(input("enter the side of the triangle"))
area()

