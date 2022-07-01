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

