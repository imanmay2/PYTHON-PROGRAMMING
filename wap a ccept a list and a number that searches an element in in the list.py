li=eval(input("enter the list you want to enter"))
print("tThe list you have entered is")
print(li)
n=int(input("enter the number you want to search"))
if(n in li):
    print(n,"is present in the list at index",li.index(n))
else:
    print(n,"is not present in the list")
