li=eval(input("enter the list you want to enter"))
for i in range(0,len(li)):
    if(li[i]>10):
        li.remove(li[i])
        li.insert(i,10)
print("the updated list is",li)
