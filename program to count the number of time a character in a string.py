#To count the number of each string in a dictinary..
str1=input("Enter the number")
d=dict()
for i in str1:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
