def sum(n):
    if(n==1):
        return(1)
    else:
        return(sum(n-1)+n)
n=int(input("enter the natural number"))
print("the sum of the first",n,"natural number is",sum(n))

