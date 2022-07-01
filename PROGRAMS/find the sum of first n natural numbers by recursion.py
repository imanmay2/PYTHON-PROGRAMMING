def sum_natural(n):
    if(n==1):
        return 1
    else:
        return(n+sum_natural(n-1))
n=int(input("enter the last natural number "))
x=sum_natural(n)
print("the sum of the natural number is",x)
