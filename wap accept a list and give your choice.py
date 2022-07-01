while(1):
    print("1.append an element")
    print("2.Insert an element")
    print("3.Appemd a list to an element")
    print("4.modify  an element")
    print("5.delete an existing element of an position")
    print("6.delete a existing element with a value an element")
    print("7.sorting an element in ascending order")
    print("8.sort ist in desecing")
    print("9.display the list")
    print("10.exit")
    choice=int(input("enter your choice"))
    li=eval(input("enter the list you want"))
    li2=li
    if(choice==1):
        n=int(input("enter the element you want to append"))
        li.append(n)
        print("updated list is",li)
    elif(choice==2):
        ind=int(input("enter the index "))
        item=input("enter the item")
        li.insert(ind,item)
        print("updated list is",li)
    elif(choice==3):
        lst=eval(input("enter the list you want to append"))
        li.extend(lst)
        print("updated list is",li)
    elif(choice==4):
        ind=int(input("enter the ind"))
        re=int(input("enter the value"))
        li.pop(ind)
        li.insert(ind,re)
        print("updated list is",li)
    elif(choice==5):
        ind=input("enter the index")
        li.pop(ind)
        print("updated list is",li)
    elif(choice==6):
        item=input("enter the item you want")
        li.remove(item)
        print("updated list is",li)
    elif(choice==7):
        li.sort()
        print("updated list is",li)
    elif(choice==8):
        li.sort(reverse=True)
        print("updated list is",li)
    elif(choice==9):
        print("your entered list is",li2)
    elif(choice==10):
        break
    else:
        print("wrong input")
    
