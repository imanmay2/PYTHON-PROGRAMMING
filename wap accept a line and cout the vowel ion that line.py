str1=input("enter a sentence")
ct=0
for i in str1:
    if(i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U"):
        ct+=1
print("the count of the vowel in that entered sentence are",ct)
