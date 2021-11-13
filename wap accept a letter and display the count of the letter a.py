#wap accept a word and count number of "a" letter in that word
str1=input("enter the word")
ct=0
for i in str1:
    if(i=="a" or i=="A"):
        ct=ct+1
print("the count of the letter a is",ct)
