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