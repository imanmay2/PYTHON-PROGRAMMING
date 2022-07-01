r=int(input("row"))
c=int(input("coloumn"))
l=[]
print("[")
for i in range(r):
    print("[",end=' ')
    for j in range(c):
        print(l[i][j],end=' ')
    print("]")
print("]")
        
