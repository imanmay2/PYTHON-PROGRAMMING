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


#5.WAP THAT WILL ASK THE USERS TO INPUT THE FIRST DAY OF THE YEAR AND PRINT ANY DAY FROM 2-365 BY USER'S CHOICE.
f=input("Enter the first day of the year").upper()
li=['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THRUSDAY','FRIDAY','SATURDAY']
n=int(input("Enter any day in-between 2-365"))
if(n<1 and n>365):
    print("INVALID DAY NUMBER!!!!PLEASE SELECT DAY IN-BETWEEN 2-365")
else:
    st=li.index(f)
    day=(n%7)+st-1
    if(day>=7):
        day=day-7
    print("DAY NUMBER OF",n,"IS",li[day])


# 6.1 FOOT = 12 INCHES. WRITE THE FUNCTIONS TO CONVERT FOOT TO INCHES AND VICE-VERSA..

    
