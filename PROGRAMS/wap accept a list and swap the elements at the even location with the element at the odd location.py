li=eval(input("enter the list you want to enter"))
print("the original list you have entered is")
print(li)
l=len(li)
if(l%2!=0):
    l=l-1
for i in range(0,l,2):
    print(i,i+1)
    li[i],li[i+1]=li[i+1],li[i]
print("list after swapping is")
print(li)
