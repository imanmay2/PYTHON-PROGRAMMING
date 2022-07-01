L1=eval(input("enter the list you want to enter"))
L2=eval(input("enter the second list you want"))
m1=max(L1)
m2=max(L2)
if(m1>m2):
    print("The first list contains the maximum elememt",m1,"at index",L1.index(m1))
else:
    print("The second list contains the maximum elememt",m2,"at index",L2.index(m2))
    
    
