#wap create a function to check whether the entered no. is divisible by 7
def check(num):
    if(num%7==0):
        print(num,"is divisible by 7")
    elif(num%7!=0):
        print(num,"is not divisible by 7")
num=int(input("enter the number you want to enter"))
check(num)
