# HELLO EVERYONE....THESE ARE FEW PROGRAMS FROM THE EXCERCISE OF FILE IO...HOPE YOU WILL ENJOY IT.
# QUESTIONS ALONG WITH THEIR SOLUTIONS ARE HERE..

#1. Wap that reads a text file  and creates another text file that is identical except that every sequence of consecutive blank spaces
# is replaced by a single step.
import pickle
import csv
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


#12.Write a program o count the letters present in the file upto $ sign.
with open("dollar.txt") as o:
    ct=0
    for i in o.read():
        if(i!=' ' and i!="$"):
            ct+=1
        elif(i=="$"):
            break
print("NUMBER OF CHARACTERS PRESENT IN THE FILE UPTO $ CHARACTERS IS AS FOLLOWS: ",ct)

#14. Write a program that appends any dictionary from the user in a .dat file
member=dict()
ans='y'
while ans=="y":
    with open("ex.dat","wb") as g:
        mem=int(input("ENTER THE MEMBER NO. : "))
        name=input("ENTER THE NAME OF THE MEMBER: ")
        member["MemberN0."]=mem
        member["Name"]=name
        pickle.dump(member,g)
        ans=input("DO YOU WANNA ENTER MORE ENTRIES: ??")

#15. write a method to search and display the content in a pickled file staff.dat where staffcode key of the dictionary is matching  with "S0105"
def display():
    staff=dict()
    with open("staff.dat","wb") as st:
        print("HOW MANY ENTRIES????YOU WANNA ENTER????")
        n=int(input())
        for i in range(n):
            staff_code=input("ENTER THE STAFF CODE: ")
            staff_name=input("ENTER THE NAME OF THE STAFF: ")
            staff["Staff_Code"]=staff_code
            staff["Name"]=staff_name
            pickle.dump(staff,st)
    with open("staff.dat","rb") as dk:
        code=input("ENTER THE CODE OF THE STAFF MEMEBER: ")
        try:
            while True:
                s=pickle.load(dk)
                if(s["Staff_Code"]==code):
                    print(s)
        except EOFError:
            dk.close() 
display()




#19. Program that will print exactly those line which conatins 5 words in that file.
with open("lines.txt") as f:
    ct=1
    for i in f.readlines():
        for j in i:
            if(j==' '):
                ct+=1
                if(ct==5):
                    print(i)


#20. write a program to read a csv file which contains a tab delimiter.
with open("result.csv","r") as gh:
    read=csv.reader(gh,delimiter='|')
    for i in read:
        print(i)

#21. write a program to write a nested list and write it on a csv file. after that display the content that has been written over there.
with open("ress.csv","w") as dh:
    fh=csv.writer(dh)
    li=[
        ["Name","Class","Roll"],
        ["Manmay","XII","02"],
        ["Soumya","X","04"]
    ]
    fh.writerows(li)
with open("ress.csv","r") as jh:
    fg=csv.reader(jh)
    for i in fg:
        print(i)
        
