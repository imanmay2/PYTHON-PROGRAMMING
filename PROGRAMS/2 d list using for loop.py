l=[]
r=int(input("enter the row"))
c=int(input("enter the coloumn"))
for i in range(r):
    row=[]
    for j in range(c):
        ele=eval(input("enter  a element"))
        row.append(ele)
    l.append(row)
print(l)
