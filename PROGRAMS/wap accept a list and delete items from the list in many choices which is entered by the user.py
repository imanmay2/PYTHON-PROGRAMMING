li=eval(input("enter the list"))
print("delete menu")
print("1. remove a single element using item")
print("2. removing element using index value")
print("3. removing a sublist")
print("4. EXIT")
while(1):
    choice=int(input("enter your choice please"))
    if(choice==1):
        ele=int(input("enter the element you want to remove from the original one"))
        li.remove(ele)
        print("the list updated list is",li)
    elif(choice==2):
        idx=int(input("enter the index value of the element you wan to remove"))
        li.pop(idx)
        print("the list updated list is",li)
    elif(choice==3):
        u=int(input("enter the upper element's index value"))
        l=int(input("enter the lower element's index value"))
        del li[u:l]
        print("updated list is",li)
    elif(choice==4):
        break
    else:
        print("invalid choice! please enter a valid one from 1 to 4")
print("PROGRAM FINISHED")

        
        
