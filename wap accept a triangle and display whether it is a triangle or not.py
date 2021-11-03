n1=float(input("enter the side"))
n2=float(input("enter the side"))
n3=float(input("enter the side"))
if(n1+n2>n3 or n1+n3>n2 or n2+n3>n1):
    print("it is a triangle")
    s=(n1+n2+n3)/2
    area=(s*(s-n1)*(s-n2)*(s-n3))**0.5
    print("area of the triangle is",area)
else:
    print("not a triangle")


  wap accept the coofiecient of a, b, c x2+bx+c.
  display it's roots...
