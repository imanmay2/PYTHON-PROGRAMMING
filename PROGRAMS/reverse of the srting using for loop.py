str1=input("enter the string")
print("the reverse of the string is")
l=len(str1)
for i in range(-1,-l-1,-1):
    print(str1[i],end="")
