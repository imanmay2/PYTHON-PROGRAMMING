lst=[]
li=eval(input("enter the list you wan to enter"))
n=int(input("enter the number you wan to increment in the list"))
for i in li:
    l=i+n
    lst.append(l)
print("the new list after incrementing is",lst)
    
