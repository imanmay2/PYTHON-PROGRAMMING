def power(x,n):
    return x**n
def fact(n):
    if(n==1):
        return n
    else:
        return n*fact(n-1)
sum=0
x=int(input("enter the number"))
n=int(input("enter the range"))
for i in range(1,n+1):
    a=power(x,i)/fact(i)
    sum=sum+a
print("the sum of the series is",sum)
