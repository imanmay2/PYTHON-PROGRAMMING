def convert(m,u):
    if(u=="celcius" or u=="c" or u=="C" or u=="Celcius" or u=="CELCIUS"):
        f=((9*m)/5)+32
        print("the converted temperature from celcius to farenheit is",f,"F")
    elif(u=="farenheit" or u=="f" or u=="F" or u=="FARENHEIT" or u=="Farenheit"):
        c=(5*(m-32))/9
        print("the converted temperature from the farenheit to celcius is",c,"C")
m=float(input("enter the value of the temperature you want to enter"))
u=input("enter the unit of the above entered value")
convert(m,u)


