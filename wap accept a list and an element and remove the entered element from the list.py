li=eval(input("enter the list you want to enter"))
print("Original list you entered is")
print(li)
ele=int(input("enter the elememt you want to remove"))
if(ele not in li):
    print(ele,"not in list")
else:
    for i in li:
        if(i==ele):
            li.clear(i)
    print("list removing",ele,"is",li)
     
