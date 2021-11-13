def natural(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
n=int(input("enter the last value of the sum"))
x=natural(n)
print("the sum of the natural no. is",x)
