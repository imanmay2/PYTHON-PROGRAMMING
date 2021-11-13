d="123456789"
f=0
str1=input("enter a string")
for i in str1:
    if(i in d):
        print(str1,"contains digit")
        f=1
        break
if(f==0):
    print(str1,"doesn't contains digit")
