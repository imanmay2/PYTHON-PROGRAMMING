def area(circum):
    r=circum/(2*3.14)
    area=3.14*r**2
    print("radius of the circle is",r)
    print("area of the circle is",area)
circum=float(input("enter the circumference of the circle"))
area(circum)
