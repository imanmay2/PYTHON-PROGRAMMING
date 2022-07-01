ans="yes"
while(ans=="yes"):
    n=int(input("enter the number"))
    for i in range(1,11):
        print(i,"*",n,"=",n*i)
    ans=input("wish to continue")
