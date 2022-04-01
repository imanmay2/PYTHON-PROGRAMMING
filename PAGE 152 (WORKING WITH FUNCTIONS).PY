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
