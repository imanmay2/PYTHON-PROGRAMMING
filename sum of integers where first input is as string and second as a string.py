n=int(input("Enter the number you want"))
str1=input("Enter the string which must have numbers")
s=''
d='1234567890'
for i in str1:
    if(i in d):
        s+=i
print("Sum of the two integers now is as follows",  n+int(s))