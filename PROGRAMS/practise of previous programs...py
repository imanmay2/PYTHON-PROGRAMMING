# 1) a). Write a program in python to print hello.
print("HELLO")


#1) b). write a program in python to make addition of two numbers.
a=10
b=6
print("Addition of two numbers are",a+b)


#1) c). write a program python to concantenate two strings.
f="Amit"
l=" Debsharma"
print("The concatenation of two strings is",f+l)


#2) write a program in python to take input from the user and print their sum.
x=float(input("Enter the first number"))
y=float(input("enter the second number"))
print("The sum of the two numbers are",x+y)


#3) write a program in python to obtain the length and breath of rectangle and print the area.
L=float(input("enter the length of the rectangle"))
B=float(input("Enter the breath of the rectangle"))
print("The area of the rectangle is",L*B)


#4) write a program in python to print the the largest of two different number.
X=int(input("enter the first number"))
Y=int(input("enter the second number"))
print("The largest number from the entered numbers is",max(X,Y))


# 5) write a program in python to find the area of a triangle by taking inputs of sides from the user.
p=float(input("Enter the side of the triangle"))
q=float(input("Enter the side of the triangle"))
r=float(input("Enter the side of the triangle"))
s=(p+q+r)/2
area=(s*(s-q)*(s-p)*(s-r))**0.5
print("The area of the triangle is",area)
