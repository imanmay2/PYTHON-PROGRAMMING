li=[]
l=[]
n=10
for i in range(1,n+1):
    num=int(input("enter the number you want"))
    l.append(num)
    if(num%2==0):
        num=num*0.5
        li.append(num)
    else:
        num=num*2
        li.append(num)
print("The original list is",l)
print("the new generated list is",li)
