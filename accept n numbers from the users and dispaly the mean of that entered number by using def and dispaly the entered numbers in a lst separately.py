def mean(n):
    li=[]
    s=0
    for i in range(1,n+1):
        num=int(input("enter the number"))
        li.append(num)
        s=s+num
    m=s/n
    print("The mean of the entered number is",m)
    print(li)
n=int(input("enter the range of the number you want to enter "))
mean(n)

        
