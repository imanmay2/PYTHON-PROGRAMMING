str1=''
alphab=0
num=0
str1=input("enter the elements of string")
l=len(str1)
for i in range(0,l):
    if str1[i].isalpha():
        alphab=alphab+1
    elif str[i].isdigit():
        num=num+1
print("no. of the digit",num)
print("no. of alhabet",alphab)
