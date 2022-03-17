li=[]
r=int(input("Enter the row"))
c=int(input("Enter the coloumn"))
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input("Element"+str(i)+","+str(j)+":"))
        row.append(ele)
    li.append(row)
print("List created as follows",li)
