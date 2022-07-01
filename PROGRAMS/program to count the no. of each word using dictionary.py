#To count the number of each word in a dictionary..
str1=input("Enter the string")
d=dict()
s=str1.split()
for i in s:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
