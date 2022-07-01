def maxi(a,b,c):
    if(a>b and a>c):
        return(a)
    elif(b>c):
        return(b)
    else:
        return(c)
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
x=maxi(a,b,c)
print(x,"is the greatest number of all")