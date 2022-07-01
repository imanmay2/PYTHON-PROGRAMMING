print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.square")
print("6.square root")
print("7.cube")
print("8.cube root")
choice=int(input("sir please enter your choice"))
if(choice>=1 and choice<=8):
    if(choice==1):
        num1=int(input("enter the number"))
        num2=int(input("enter the second number"))
        res=num1+num2
        print("the addition of the numbers entered are",res)
    elif(choice==2):
        if(num1>num2):
            num1=int(input("enter the number"))
            num2=int(input("enter the second number"))
            res=num1-num2
        else:
            num1=int(input("enter the number"))
            num2=int(input("enter the number"))
            res=num2-num1
        print("the subtraction of the numbers entered are",res)
    elif(choice==3):
        num1=int(input("enter the number"))
        num2=int(input("enter the second number"))
        res=num1*num2
        print("the multiplication of the numbers entered are",res)
    elif(choice==4):
        num1=int(input("enter the number"))
        num2=int(input("enter the second number"))
        res=num1/num2
        print("the division of the two numbers entered are",res)
    elif(choice==5):
        num=int(input("enter the number"))
        res=num**2
        print("the sqauare root is",int(res))
    elif(choice==6):
        num=int(input("enter the number"))
        res=num**(1/2)
        print("the square root of the entered number is",res)
    elif(choice==7):
        num=int(input("enter the number"))
        res=num**3
        print("the cube of the entered number is",res)
    else:
        num=int(input("enter the number"))
        res=num**(1/3)
        print("the cube root of the entered number is",res)
else:
    print("sorry! you have not entered your choice from 1 to 8")
