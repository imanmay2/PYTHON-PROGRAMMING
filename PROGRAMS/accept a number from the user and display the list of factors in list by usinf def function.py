def fact(n):
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
n=int(input("enter a number"))
print("the factors are")
l=[]
fact(n)
print(l)
