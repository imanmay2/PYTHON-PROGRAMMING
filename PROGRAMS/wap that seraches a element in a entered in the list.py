li=eval(input("enter a list"))
print(li)
n=int(input("enter the item to be searched"))
for i in li:
    if(i==n):
        print("item is found in the list")
        break
else:
    print("not found in the list")
