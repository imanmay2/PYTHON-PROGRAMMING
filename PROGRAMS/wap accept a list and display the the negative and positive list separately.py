li=eval(input("enter the list"))
lp=[]
ln=[]
for i in li:
    if(i<0):
        ln.append(i)
    else:
        lp.append(i)
print("the entered list is",li)
print("the positive list is",lp)
print("the negative list is",ln)
