def sum1():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    sum=a+b
    print("the sum of the two numbers is ",sum)
def sum2(a,b):
    sum=a+b
    print("The sum of the two numbers is ",sum)
def sum3(a,b):
    sum=a+b
    return(sum)

print("calling to the first function")
sum1()
print("calling to the second function")
a=int(input("enter the number"))
b=int(input("enter the number"))
sum2(a,b)
