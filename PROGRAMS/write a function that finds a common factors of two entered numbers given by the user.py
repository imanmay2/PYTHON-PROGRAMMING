def common_factors():
    l=[]
    l1=[]
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
    s=set(l)
    for i in range(1,n1+1):
        if(n1%i==0):
            l1.append(i)
    s1=set(l1)
    common_factor=s.intersection(s1)
    return common_factor
n=int(input("enter the first number that you wish"))
n1=int(input("enter the second number that you wish"))
print("The common factors of both the numbers are",common_factors())
            
            
