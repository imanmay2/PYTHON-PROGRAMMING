#wap to input a line and print the word which has the length as 4.
str1=input("enter the line you want to enter")
s=str1.split()
for i in s:
    if(len(i)==4):
        print(i)
