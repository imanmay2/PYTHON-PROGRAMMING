str1=input("enter the string")
l=0
u=0
for i in str1:
    if(i.islower()):
        l=l+1
    elif(i.isupper()):
        u=u+1
print("the count of the lower and upper case letters are ",l,u)
