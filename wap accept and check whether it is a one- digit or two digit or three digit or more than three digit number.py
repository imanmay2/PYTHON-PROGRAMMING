#wap accept a number and check whether it is 1 digit two digir or more
num=int(input("enter the number"))
if(num>-10 and num<10):
    print(num,"is the one-digit number")
elif(num>9 and num<100):
    print(num,"is a two digit number")
elif(num>99 and num<1000):
    print(num,"is a three digit number")
else:
    print(num,"is more than three digit number")
