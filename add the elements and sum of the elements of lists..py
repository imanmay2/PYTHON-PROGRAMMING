l=[]
sum=0
maxl=int(input("enter the range of the list"))
for i in range(1,maxl+1):
    num=int(input("enter the element of list"))
    l.append(num)
for j in range(0,maxl):
    sum=sum+l[j]
print(sum)
