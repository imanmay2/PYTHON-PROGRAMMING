li=[]
for i in range(10):
    num=int(input("Enter the number"))
    li.append(num)
for i in li:
    if(type(i**0.5)==type(0.5)):
        print(i,end=' ')
