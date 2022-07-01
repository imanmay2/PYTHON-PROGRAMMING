str1=input("enter the string")
ct=0
c=0
for i in str1:
    if(i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U"):
        ct=ct+1
    else:
        c=c+1
print("no. of vowels is",ct)
print("count of consonant is",c)
        
        
