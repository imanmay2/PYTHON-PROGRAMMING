#wap that will accept some datas from the user and print it accordingly to the user.
import pickle
stu=dict()
with open("stu1.dat","wb") as f:
    ans="y"
    while ans=="y":
        r=float(input("ENTER THE ROLL NO.: "))
        n=input("ENTER THE NAME OF THE STUDENT: ")
        m=int(input("ENTER THE MARKS OF THE STUDENT: "))
        stu["roll"]=r
        stu["name"]=n
        stu["marks"]=m
        pickle.dump(stu,f)
        ans=input("WANNA ENTER MORE RECORDS THEN TYPE Y ELSE N: ")
        print()
        print()
        print()
        print()
print("FILE READED SUCCESFULLY...READ FILE IS PRINTED BELOW: ")
with open("stu1.dat","rb") as f1:
    try:
        while True:
            print(pickle.load(f1))
    except EOFError:
        f1.close()
        print()
        print()


#wap to open the file stu1.dat and search records with n roll numbers.If found, display the records.
import pickle
li=[1,2]
f=0
with open("stu1.dat","rb") as f2:
    try:
        while True:
            dic=pickle.load(f2)
            if(dic["roll"] in li):
                print(dic)
                f=1
    except EOFError:
        if(f==0):
            print("NOT FOUND THE ROLL NUMBER FROM THE LIST....")
        f2.close()

#wap that will print the records which are having more than 81 marks.
f=0
with open("stu1.dat","rb") as f3:
    try:
        while True:
            d=pickle.load(f3)
            if(d["marks"]>81):
                print(d)
                f=1
    except EOFError:
        if(f==0):
            print("NO RECORDS FOUND IN THE DATABASE.....")
            f3.close()            