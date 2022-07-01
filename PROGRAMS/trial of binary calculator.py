#decimal to binary conversion conversion
deci=int(input("Enter the number"))
str1=''
while(deci!=0):
    r=deci%2
    str1=str1+str(r)
    deci=deci//2
print(str1)

