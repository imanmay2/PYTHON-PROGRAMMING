# HELLO EVERYONE....THESE ARE FEW PROGRAMS FROM THE EXCERCISE OF FILE IO...HOPE YOU WILL ENJOY IT.
# QUESTIONS ALONG WITH THEIR SOLUTIONS ARE HERE..

#1. Wap that reads a text file  and creates another text file that is identical except that every sequence of consecutive blank spaces
# is replaced by a single step.
with open("space.txt","r") as f:
    li=f.read().split()
    print(li)
    for i in li:
        print(i,end=' ')
        

#2. create a file named as sports.dat that conatins ....Event ~ Participants.Create another file named Atheletic.dat copying only those
#records from sports.dat where the event nameis "Atheletics"



#3. 

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


#8.WAP that appends the contents of one file to another.Have the program take the filename from the user
file_name=input("ENTER THE FILE_NAME: ")
with open(poem.txt,"r") as y:
    str1=y.read()
with open(file_name.txt,"w") as j:
    j.write(str1)


#9. Write a function DISPLAY() and this will display those words which are less than 4.
def display():
    with open("poem1.txt") as f:
        for i in f.read().split():
            if(len(i)<4):
                print(i)
display()



#10. write a program that reads character from the keyboard one by one , all lower case letters get stored in the lower.txt and similarly
# for upper and others file
s=input("ENTER THE STRING: ")
for i in s:
    if(i.islower()):
        with open("lower.txt","a") as l:
            l.write(i)
    elif(i.isupper()):
        with open("upper.txt","a") as w:
            w.write(i)
    else:
        with open("others.txt","a") as h:
            h.write(i)
    
            

# 11. Write a function to count the number of lines starting with A in lines.txt.
with open("lines.txt") as f:
    ct=0
    for i in f.readlines():
        if(i[0]=="A"):
            ct+=1
    print("No. of lines starting with A is: ",ct)


#19. Program that will print exactly those line which conatins 5 words in that file.
with open("lines.txt") as f:
    ct=1
    for i in f.readlines():
        for j in i:
            if(j==' '):
                ct+=1
                if(ct==5):
                    print(i)
        

