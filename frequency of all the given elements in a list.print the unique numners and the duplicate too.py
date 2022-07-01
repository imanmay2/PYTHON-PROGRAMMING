# frequency of all the given elements in a list.print the unique numners and the duplicate too
li=eval(input("Enter the list"))
a=[]
u=[]
d=[]
for i in li:
    if(i not in a):
        a.append(i)
        ct=li.count(i)
        print("Frequency of the element",i,"is",ct)
        if(ct>1):
            d.append(i)
        elif(ct==1):
            u.append(i)
print("Unique list is as follows",u)
print("Duplicate list is as follows",d)
        
            
    
