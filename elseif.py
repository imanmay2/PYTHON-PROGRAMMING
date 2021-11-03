name=input("enter any name").lower()
names=eval(input("enter the list of names you want to enter"))
if(name in names):
    print(name,"is present in the list of the names")
else:
    print(name,"is not present in the list of names")