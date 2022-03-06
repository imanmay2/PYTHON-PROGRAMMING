# inserting numbers in this 2-D list.

r=int(input("Enter the rows to be entered in the 2-D list"))
c=int(input("Enter the columns to be entered in the 2-D list"))
li=[]
for i in range(r):
    l=[]
    for j in range(c):
        ele=int(input("Enter the element"))
        l.append(ele)
    li.append(l)
print("THE 2-D LIST IS AS FOLLOWS")
print(li)
