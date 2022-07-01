#wap create a list with 15 elements check whether they are digit or string and count
#and count them.
dig="0123456789"
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
li=[]
d=0
al=0
for i in range(1,16):
    num=input("enter the element you want")
    li.append(num)
print("the list created is",li)
for i in li:
    if(i in dig):
        d=d+1
    elif(i in alpha):
        al=al+1
print("the count of the digit in the list is",d)
print("the count of the alphabet in the list is",al)
