# printing the words which starts with vowels.
print("The first letter of the word which starts with vowel are as follows:")
with open("main.txt") as f:
    data=f.read().split()
    for i in range(0,len(data)):
        if(data[i][0]=="a" or data[i][0]=="e" or data[i][0]=="i" or data[i][0]=="o" or data[i][0]=="u" or data[i][0]=="A" or data[i][0]=="E" or data[i][0]=="I" or data[i][0]=="O" or data[i][0]=="U"):
            print(data[i])
