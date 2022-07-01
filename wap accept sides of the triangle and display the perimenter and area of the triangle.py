n1=float(input("enter the first of the triangle"))
n2=float(input("enter the second of the triangle"))
n3=float(input("enter the thir4d of the triangle"))
per=(n1+n2+n3)
s=per/2
area=(s*(s-n1)*(s-n2)*(s-n3))**0.5
print("perimeter of the triangle is",per)
print("area of the triangle is",area)
