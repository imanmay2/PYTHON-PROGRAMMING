# wap accept a string and replace all vowel with "*".
str1=input("enter the srring")
for i in str1:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        str1=str1.replace(i,'*')
print("the new string is",str1)
        
