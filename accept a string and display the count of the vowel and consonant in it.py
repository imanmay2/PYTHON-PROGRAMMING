str1=input("enter the string to count how many are vowel and consonant")
v=0
c=0
for i in str1:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        v=v+1
    else:
        c=c+1
print("the count of the vowels are",v)
print("the count of the consonant",c)
        
