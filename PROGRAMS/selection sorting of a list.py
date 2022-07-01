li=eval(input("Enter the list"))
for i in range(0,len(li)-1):
    for j in range(0,len(li)):
        if(li[j]<li[i]):
            t= li[j]
            li[j]=li[i]
            li[i]=t
print("List after sorting is as follows",li)
                   
