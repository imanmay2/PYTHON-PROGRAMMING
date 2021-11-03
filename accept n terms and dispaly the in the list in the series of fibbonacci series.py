def fib(n):
    a=0
    b=1
    ct=2
    for i in range(3,n+1):
        c=a+b
        ct=ct+1
        l.append(c)
        if(num==c):
            print("the position of",num,"is",ct)
            break
        a=b
        b=c
n=int(input("enter the range of the fibbonacci series"))
l=[0,1]
num=int(input("enter the number to find the position"))
fib(n)
print(l)



