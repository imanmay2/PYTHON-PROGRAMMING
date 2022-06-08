#1.CREATING A BINARY FILE WHERE 2 DICTIONARIES ARE INSERTED.. and also display the things which are inserted in that .dat file..with the help of try and catch.
import pickle
emp1={"Empno":1201,"Name":"Anushree","Age":25,"Salary":47000}
emp2={"Empno":1211,"Name":"Zoya","Age":30,"Salary":48000}
with open("emp.dat","wb") as f:
    pickle.dump(emp1,f)
    pickle.dump(emp2,f)
    print("File has been successfully added to the .dat extension")
with open("emp.dat","rb") as f1:
    try:
        while True:
            print(pickle.load(f1))
    except EOFError:
        f1.close()

#2.WAP to get student data such as roll no., name and marks from the user and write onto the binaryfile.The program should be able 
#to get the data from the user and write onto as long as user wants.AND ALSO PRINT THE DICTIONARIES IN THE PYTHON SHELL.
stu={}
with open("stu.dat","wb") as f2:
    ans="y"
    while ans=="y":
        r=int(input("Enter the roll number please: "))
        n=input("Enter the name please: ")
        m=float(input("Enter the marks please: "))
        stu["Roll"]=r
        stu["Name"]=n
        stu["Marks"]=m
        pickle.dump(stu,f2)
        ans=input("DO YOU WANNA CONTINUE????ENTER y FOR YES OR n FOR NO")
with open("stu.dat","rb") as f3:
    try: 
        while True:
            print(pickle.load(f3))
    except EOFError:
        f3.close()

#3.Write A program from the file named myfile.info ..print the letters from starting until the letter 'o' is encountered.
with open("myfile.info","wb") as f4:
    pickle.dump(input("Enter the string you wanna enter: "),f4)
with open("myfile.info","rb") as f5:
    li=pickle.load(f5).split('o')
    print(li[0])
    print(li)



