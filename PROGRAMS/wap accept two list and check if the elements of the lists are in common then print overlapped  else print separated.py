li1=eval(input("enter the list"))
li2=eval(input("enter the second list"))
f=0
for i in li1:
    if(i in li2):
        print("overlapped")
        f=1
        break
if(f==0):
    print("separated")
