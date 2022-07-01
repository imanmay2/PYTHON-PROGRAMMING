def factor(num):
    li=[]
    for i in range(1,num+1):
        if(num%i==0):
            li.append(i)
    return(li)
num=int(input("enter the number you want to enter "))
x=factor(num)
print("the factors are as follows:",x)
            
