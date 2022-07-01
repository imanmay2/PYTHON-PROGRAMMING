str1=input("enter the string you wan to enter")
rev=-1
f=0
for i in str1:
    if(i==str1[rev]):
        rev-=1
    else:
        print(str1,"is not palindrome")
        f=1
        break
if(f==0):
    print(str1,"is palindrome")
