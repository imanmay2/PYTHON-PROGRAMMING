str1=input("enter the string you want to enter")
l=len(str1)
str2=""
for i in range(0,l):
    if(i%2==0):
        str2+=str1[i].lower()
    else:
        str2+=str1[i].upper()
print("the alternative capitalized string is",str2)
        
    

