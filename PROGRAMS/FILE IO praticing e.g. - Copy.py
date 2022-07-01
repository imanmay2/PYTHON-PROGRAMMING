#1. Display the size of the file after removing EOL characters,leading and trailing whitespaces and blank lines.
with open("poem1.txt","r") as f:
    str1=f.read()
    ct=0
    for i in str1:
        ct=ct+1
    c=0
    k=str1.split()
    for j in k:
        c=c+1
    print("SIZE OF FILE AFTER REMOVING THE EOL IS : ",c)
    print("SIZE OF FILE BEFORE REMOVING THE EOL IS : ",ct)
    print()
    print()

    
#2. READING A COMPLETE FILE IN A LIST.
with open("poem1.txt") as f:
    print(f.readlines())
    print()
    print()


#3. To display how many bytes does  a particular file consuming in your Computer.
with open("poem1.txt") as f:
    print(len(f.read()))
    print()
    print()


#4.To display how many lines does a file contain...
with open("poem1.txt") as f:
    print(len(f.readlines()))
    print()
    print()

#5. Create a file which can hold names of n students.
with open("Student_File_IO.dat","w") as f:
    for i in range(int(input("Enter how many student's name you wanna insert: "))):
        f.write(input("ENTER THE NAME PLEASE: "))
        f.write('\n')
    print()
    print()

#5. Create a file with some names separated names by newline characters without using the write() function.
with open("Student1_Fie_IO.txt","w") as f:
    li=[]
    for i in range(int(input("Enter how many names you wanna enter: "))):
        li.append(input("Enter the name : ")+'\n')
    f.writelines(li)
    print()
    print()

#6. program to input the roll o. names and marks of the student of a class and store the details in the file name marks.txt.
with open("marks.txt","w") as f:
    for i in range(int(input("How many inputs you wanna enter: "))):
        roll=float(input("ENTER YOUR ROLL NO. : "))
        marks=float(input("ENTER YOUR MARKS : "))
        f.write(input("ENTER YOUR NAME: ")+str(roll)+str(marks))
        f.write('\n')

#7. Program to read a text file line by line and display each word  separated by #.
with open("poem.txt","r") as f:
    line=''
    while line:
        line=f.readline()
        for i in line.split():
            print(i,"#")

#8. Program to count the vowel and consonant from any created file like poem1.txt
with open("poem1.txt") as f:
    str1=f.read()
    v="AEIOUaeiou"
    vo=0
    co=0
    for i in str1:
        if(i in v):
            vo+=1
        else:
            co+=1
    print("COUNT OF VOWEL AND CONSONANT IS: ",vo,co,"RESPECTIVELY")

    



