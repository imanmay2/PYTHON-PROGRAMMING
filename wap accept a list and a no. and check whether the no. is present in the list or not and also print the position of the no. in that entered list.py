li=eval(input("enter the list you want to enter"))
print("the list you have entered is",li)
n=int(input("enter the no. you want to find in the list"))
if(n in li):
    print(n,"present in the entered list at the position of",(li.index(n))+1)
else:
    print(n,"not present in the list")
        
