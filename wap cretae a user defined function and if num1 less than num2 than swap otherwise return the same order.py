def num(a,b):
    if(a<b):
        a=a+b
        b=a-b
        a=a-b
        return(a,b)
    else:
        return(a,b)
a=int(input("enter the number"))
b=int(input("enter the number"))
x=num(a,b)
print(x)
        
