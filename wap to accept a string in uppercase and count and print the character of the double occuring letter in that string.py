#wap to accept a string in uppercase and count and print the character of the double occuring letter in that string.
str1=input("Enter the string you want").upper()
ct=0
d=''
for i in range(0,len(str1)-1):
    if(str1[i]==str1[i+1]):
        ct=ct+1
        d=d+(str1[i]+' ')
print("Count of such words are as follows",ct)
print("Double occuring words are as follows",d)

