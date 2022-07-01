li=eval(input("enter the list you want to enter"))
l=[]
for i in li:
    if i not in l :
        l.append(i)
print("the original list after duplicating is")
print(l)
