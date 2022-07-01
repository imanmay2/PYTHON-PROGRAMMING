# wap accept a number and check whether it is greater 10 and even number.
a=int(input("enter the number"))
if(a>10):
    if(a%2==0):
        print("number is greater than 10 and even number")
    else:
        print("number is not even byt greater than 10")
else:
    if(a%2==0):
        print("number is less than 10 and even number")
    else:
        print("number is not even but less than 10")
        
