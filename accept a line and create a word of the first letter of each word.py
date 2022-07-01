#WAP accept a sentence and display a word forming by each first letter of the 
#word of the sentence..
line=input("enter the sentence")
li=line.split()
ct=len(li)
print(li)
print("the count of the word entered is",ct)
for i in range(0,ct):
    print(li[i][0],end='')

