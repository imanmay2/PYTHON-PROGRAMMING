w="mississippi"
str1=input("enter the letter")
s=''
for i in range(0,len(w)):
    if(w[i]==str1):
        s+=w[i].upper()
    else:
        s+=w[i]
print(s)
