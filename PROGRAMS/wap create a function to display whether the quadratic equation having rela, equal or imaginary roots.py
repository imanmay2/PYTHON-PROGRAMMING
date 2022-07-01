def equation(a,b,c):
    d=(b*b)-(4*a*c)
    if(d>0):
        return("the equation having real roots")
    elif(d==0):
        return("the equation having equal roots")
    elif(d<0):
        return("the equation having no real roots! the roots are imaginary")
a=int(input("enter the coefficient of x square"))
b=int(input("enter the coefficient of x"))
c=int(input("enter the constant term"))
x=equation(a,b,c)
print(x)
