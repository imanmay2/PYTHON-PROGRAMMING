a=eval(input("enter the tuple you want to enter"))
print("the tuple you entered is",a)
b=list(a)
c=[]
d=[]
print("the list converted from tuple is",b)
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
print(tuple(c))
print(tuple(d))
        
        
