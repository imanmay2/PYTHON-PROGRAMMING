def max(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num3):
        return num2
    else:
        return num3
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
num3=float(input("enter the third number"))
print("the biggest number from these 3 numbers is",max(num1,num2,num3))
