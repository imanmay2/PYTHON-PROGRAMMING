#A B C D E
#B C D E
#C D E
#D E
#E
#WAP to accept a string from the user and display the pattern shown above.
str1=input("Enter the string you want")
x=len(str1)
while(x>0):
    for i in str1:
        print(i,end=' ')
    print()
    str1=str1.replace(str1[0],'')
    x=x-1
    

#wap that will accept 10 names from the user and display those names that starts with the character
#entered by the user.
li=eval(input("Enter the names of 10"))
n=input("Enter the character that will be print those names from the list of 10")
for i in li:
    if(i[0]==n):
        print(i)


#wap to accept a string and change the vowel with it's next corresponding vowels
str1=input("Enter the string you want").upper()
v="AEIOU"
for i in str1:
    if(i=="U"):
        str1=str1.replace("U","A")
    elif(i in v):
        ind=v.index(i)
        str1=str1.replace(i,v[ind+1])
print("NEW STRING IS AS FOLLOWS",str1)

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

