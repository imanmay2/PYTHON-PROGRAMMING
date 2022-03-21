str1=input("enter the string").upper()
li=str1.split()
ct=0
for i in range(len(li)):
    for j in range(len(li[i])-1):
        if (chr(ord(li[i][j])+1)) == li[i][j+1]:
            ct=ct+1
            print(li[i], end=" ")
            break
print("no. of such words are as follows",ct)
