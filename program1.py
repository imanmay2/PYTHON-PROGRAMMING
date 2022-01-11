li=[]
for i in range(1,6):
    t=tuple()
    n=input("Enter the name")
    sp=n.split(",")
    for j in sp:
        t=t+(j,)
    li.append(t)
names=[li[0][0],li[1][0],li[2][0],li[3][0],li[4][0]]
names.sort()
print(names)

