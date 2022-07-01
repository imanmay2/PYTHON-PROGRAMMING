# 2. wap to count the number of times of a given character in the given string by the user.
line=input("enter a line")
s=input("enter a string")
ct=0
for i in line:
    if(s==i):
        ct+=1
if(ct==0):
    print("no such",s,"is found in the",line)
elif(ct!=0):
    print("yes the string",s,"is found in the",line," .And the no. of times is",ct)
