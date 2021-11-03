n=int(input("enter the range of the program you want to give"))
li=[]

for i in range(1,n+1):
    num=int(input("enter the number you want"))
    li.append(num)
print(li)
li.sort(reverse=True)
print(li)
print("The second maximum number is",li[1])
    
