#create a function that calculate area of a circle and return the value
#accept the radius and call the above function.
def area(r):
    ar=3.14*r*r
    return ar
r=float(input("enter the radius you want"))
x=area(r)
print("the area of the circle is",x)
