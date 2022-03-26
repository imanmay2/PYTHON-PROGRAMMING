#1.WAP TO CHECK WHETHER THE VARIABLE IS ZERO NEGATIVE OR POSITIIVE.
def check(x):
    if(x<0):
        print(x,"is a negative number")
    elif(x>0):
        print(x,"is a positive number")
    else:
        print(x,"is a nuetral number")
n=int(input("Enter any number: "))
check(n)


#2.WAP that returns True if the input number is an even number , False otherwise.
n=int(input("Enter any number: "))
if(n%2==0):
    print("TRUE")
else:
    print("FALSE")


#3.WAP THAT WILL CALCULATE AND PRINT THE NUMBER OF SECONDS A YEAR HAS...
print("YEAR HAS ",365*24*3600," SECONDS")


#4.WAP THAT WILL INPUT 2 NUMBERS AND CHECK WHETHER THE FIRST NUMBER IS DIVISIBLE BY THE SECOND ONE OR NOT..
num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
if(num1%num2==0):
    print("YES!!!!FIRST NUMBER IS FULLY DIVISIBLE BY SECOND NUMBERS")
else:
    print("NOPE!!!!FIRST NUMBER IS NOT DIVISIBLE BY THE SECOND NUMBER")
    
