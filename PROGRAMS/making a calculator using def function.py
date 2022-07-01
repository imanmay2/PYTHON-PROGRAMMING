print("1. ADDITION")
print("2.SUNSTRACTIOHN")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5.LOGARITHM")
print("6. SINE")
print("7. COSINE")
print("8. EXIT")
import math
def add(n1,n2):
    return(n1+n2)
def sub(n1,n2):
    return(n1-n2)
def multi(n1,n2):
    return(n1*n2)
def div(n1,n2):
    return(n1/n2)
def log(n1):
    x=math.log10(n1)
    return(x)
def sine(n1):
    x=math.sin(n1)
    return(x)
def cosine(n1):
    x=math.cos(n1)
    return(x)
while(1):
    ch=int(input("enter your choice"))
    if(ch==1):
        n1=int(input("enter the first number"))
        n2=int(input("enter the second number"))
        print("the addition of two numbers is",add(n1,n2))
    elif(ch==2):
        n1=int(input("enter the first number"))
        n2=int(input("enter the second number"))
        print("the substraction of two numbers is",sub(n1,n2))
    elif(ch==3):
        n1=int(input("enter the first number"))
        n2=int(input("enter the second number"))
        print("the multiplication of two numbers is",multi(n1,n2))
    elif(ch==4):
        n1=int(input("enter the first number"))
        n2=int(input("enter the second number"))
        print("the division of two numbers is",div(n1,n2))
    elif(ch==5):
        n1=int(input("enter the first number"))
        print("the logarithm of one number is",log(n1))
    elif(ch==6):
        n1=int(input("enter the first number"))
        print("the sine of number is",sine(n1))
    elif(ch==7):
        n1=int(input("enter the first number"))
        print("the cosine of one number is",cosine(n1))
    elif(ch==8):
        print("PROGRAM FINISHED")   
        break
    else:
        print("Invalid number please enter a valid one ")







    