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
def F_I(f):
    i1=12*f
    return i1
def I_F(i):
    f1=i/12
    return f1
f=int(input("Enter the length in foot respectively:    "))
print("Foot entered is",f,"respective inches is",F_I(f))
i=int(input("Enter the length in inches respectively:    "))
print("Inches entered is",i,"respective foot is",I_F(i))


#7. WAP ACCEPT AN INTEGER 'N' AND DISPLAY THE SUM FROM N TO (2*N),IF IT'S NON-NEGATIVE....AND IF IT'S NEGATIVE THEN DISPLAY THE SUM FROM 
# (2*N) TO N
n=int(input("Enter the number"))#N
s1=0
if(n>0):
    for i in range(n,(2*n)+1):
        s1+=i
elif(n<0):
    for j in range(n,(2*n)-1,-1):
        s1+=j
print("THE SUM IS AS FOLLOWS",s1)

        
#8. WAP ACCEPT A DATE IN A FORMAT LIKE..MMDDYYYY....AND DISPLAY IN MONTH NAME IN FRONT IN WORDS....
#SAMPLE.....INPUT....12252019........DESIRED OUTPUT IS......DECEMBER 25, 2019
date=str(int(input("Enter the date in MMDDYYYY")))
m=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
print(m[int(date[0:2])-1], date[2:4], date[4:8])


#9. WAP CREATE A TABLE CONVERTING MILES INTO KILOMETER.

    
