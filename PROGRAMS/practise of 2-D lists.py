r=3
c=3
li=[]
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input("Enter the element"+str(i)+","+str(j)))
        row.append(ele)
    li.append(row)
print("2-D list created is as follows")
print(li)
# printing the first diagonal of the 3 by 3 2-d list
for i in range(0,len(li)):
    for j in range(0,len(li)):
        if(i==j):
            print(li[i][j])
    print()
# printing the second diagonal of the 3 by 3 2-d list
k=0
j=2
for i in range(0,len(li)):
    print(li[k][j])
    k+=1
    j-=1
    
