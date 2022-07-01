def temp(m,u):
    if(u=="c" or u=="C"):
        con=((9*m)/5)+32
        print("The converted farenheit temperature is",con,"F")
    elif(u=="f" or u=="F"):
        con=(5*(m-32))/9
        print("the converted celcius is",con,"C")
m=float(input("enter the tempertature"))
u=input("enter the temperature scale")
temp(m,u)
        