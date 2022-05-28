# HELLO EVERYONE....THESE ARE FEW PROGRAMS FROM THE EXCERCISE OF FILE IO...HOPE YOU WILL ENJOY IT.
# QUESTIONS ALONG WITH THEIR SOLUTIONS ARE HERE..

#4. Write a program to count the words 'to' and 'the' from the text file named poem1.txt.
with open("poem1.txt") as f:
    t=0
    th=0
    for i in f.read().split():
        if(i=="to"):
            t=t+1
        elif(i=="the"):
            th=th+1
    print("Count of the word 'to' and 'the' is: ",t,th,"respectively.")

#5. Write a function AMCount() that will count the number of occurence of A,a or M,m does contain in the file.
with open("ex.5.txt") as f:
    ct_a=0
    ct_m=0
    for i in f.read():
        if(i=='a' or i=="A"):
            ct_a+=1
        elif(i=='m' or i=="M"):
            ct_m+=1
    print("A or a : ",ct_a)
    print("M or m : ",ct_m)

#6. Program to count the number of uppercase alphabets present in the poem1.txt.
with open("poem1.txt") as f:
    ct=0
    for i in f.read():
        if(i.isupper()):
            ct+=1
    print("The uppercase alphabets are as follows: ",ct)

#7.Write a program that will copy one file's content to another.
 # NOTE : that user should be asked to enter the file name.
with open("poem1.txt") as f:
    str1=f.read()
with open(input("ENTER THE FILE NAME...WHERE YOU WANNA COPY : "),"w") as f1:
    f1.write(str1)

#9. Write a function DISPLAY() and this will display those words which are less than 4.
def display():
    with open("poem1.txt") as f:
        for i in f.read().split():
            if(len(i)<4):
                print(i)
display()

#10. Write a program that will input n characters from the keyboard and if the letter entered is lower , then it will get stored in the lower.txt file.similarly for others and uppercase too.
with open("poem1.txt") as f:
    for i in f.read():
        if(i.isupper()):
            with open("upper.txt","w") as f1:
                f1.write(i,end=' ')
        elif(i.islower()):
            with open("lower.txt","w") as f2:
                f2.write(i,end=' ')
        else:
            with open("others.txt","w") as f3:
                f3.write(i,end=' ')
