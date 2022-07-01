num=int(input("enter the number"))
sum=0
while(sum!=1 and sum!=4):
    rem=num%10
    sum=sum+rem*rem
    num=num//10
print(sum)
if(sum==1):
    print("happy number")
else:
    print("not a happy number")
