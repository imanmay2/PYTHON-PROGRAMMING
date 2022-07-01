def square(s):
    area=s**2
    perimeter=4*s
    return(area,perimeter)
def rectangle(l,b):
    ar=l*b
    per=l+l+b+b
    return(ar,per)
def triangle(a,b,c):
    s=(a+b+c)/2
    a1=(s*(s+a)*(s+b)*(s+c)**0.5)
    per1=2*s
    return(a1,per1)
def circle(r):
    per2=2*3.14*r
    ar2=3.14*r**2
    return(ar2,per2)
def cyclinder(r1,h):
    tsa=(2*3.14*r*h)+2*3.14*r**2
    csa=(2*3.14*r*h)
    per3=(4*3.14*r)+(2*h)
    return(tsa,csa,per3)
s=float(input("enter the side of the square"))
print("the area and perimeter of the square is",square(s))
l=float(input("enter the value"))
b=float(input("enter the value"))
print("the area and perimeter of the rectangle is",rectangle(l,b))
a=float(input("enter the value"))
b=float(input("enter the value"))
c=float(input("enter the value"))
print("the area and perimeter of the triangle is",triangle(a,b,c))
r=float(input("enter the value"))
print("the area and circumference of the circle is",circle(r))
r1=float(input("enter the value"))
h=float(input("enter the value"))
print("the total surface area , curve surface area and the perimeter of the cylinder is",cyclinder(r1,h))
