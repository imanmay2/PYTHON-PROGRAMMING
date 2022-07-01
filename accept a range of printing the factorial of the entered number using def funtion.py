def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("The factorial is",f)
n=int(input("enter the number of the factorial series"))
fact(n)
