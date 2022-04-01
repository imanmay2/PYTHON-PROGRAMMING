#1. WAP THAT WILL CREATE 2 FUNCTIONS (1) AMOUNT-IN-DOLLARS (2) DOLLAR-TO-RUPEE CONVERSION PRICE.
def amt_in_dollar():
    d=int(input("ENTER THE AMOUNT IN DOLLARS: "))
    return d
d=int(amt_in_dollar())
def convert(d):
    con=d*76
    return con
print("YOU HAVE INPUTTED DOLLAR: ",d)
print("CONVERTED IN RUPEE: ",convert(d))


#2. WAP THAT WILL CALCULATE THE VOLUME OF A BOX.USER WILL BE GIVING IT;S DEFAULT PARAMETER LIKE LENGTH, HEIGHT AND WIDTH.
def vol(l,w,h):
    v=l*w*h
    return v
l=float(input("ENTER YOUR DESIRED LENGTH"))
w=float(input("ENTER YOUR DESIRED WIDTH"))
h=float(input("ENTER YOUR DESIRED HEIGHT"))
print("VOLUME OF THE BOX IS AS FOLLOWS: ",vol(l,w,h))


#3.WAP THAT WILL CREATE A FUNCTION THAT WILL ACCEPT A NUMBER AND DISPLAY THE CUBE OF THAT NUMBER.IF THE USER HASN'T ENTERED NOTHING THEN IT SHOULD PRINT THE CUBE ROOT OF 2.
def yes(num):
    print("CUBE OF THAT NUMBER IS AS FOLLOWS: ",num**3)
def no():
    print("CUBE OF 2 IS AS FOLLOWS: 8")
str1=input("DO YOU WANT TO ENTER NUMBER").upper()
if(str1=="YES"):
    num=float(input("ENTER YOUR DESIRED NUMBER PLEASE: "))
    yes(num)
else:
    no()
# 