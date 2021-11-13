str1=input("enter the string you want to enter")
ct=0
for i in str1:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        ct=ct+1
print("the count of the vowel is",ct)
