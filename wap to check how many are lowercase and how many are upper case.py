#wap to check how many are lowercase and how many are upper case
str1=input("enter the line you want to enter")
up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upp=0
lo="abcdefghijklmnopqrstuvwxyz"
low=0
for i in str1:
    if(i in up):
        upp+=1
    elif(i in lo):
        low+=1
print("The count of uppercase and lowercase is as follows:",upp,low,"respectively")
