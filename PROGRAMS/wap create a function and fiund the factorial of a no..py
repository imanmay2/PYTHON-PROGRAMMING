def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("enter"))
x=fact(n)
print("the factorial of the number is",x)
