# Program to to a binary file called emp.dat and write into it the employee details of some employees, avilable in the form of dictionaries.
import pickle
emp1={"EMP_No.":1201,"Name":"Anushree","Age":25,"Salary":48000}
emp2={"EMP_No.":1211,"Name":"Zoya","Age":30,"Salary":46000}
emp3={"EMP_No.":1251,"Name":"Simarjeet","Age":27,"Salary":52000}
emp4={"EMP_No.":1266,"Name":"Alex","Age":29,"Salary":50000}
with open("emp.dat","wb") as f:
    pickle.dump(emp1,f)
    pickle.dump(emp2,f)
    pickle.dump(emp3,f)
    pickle.dump(emp4,f)
    print("........SUCCESSFULLY WRITTEN FOUR DICTIONARIES........")

# Program to get student data(roll no.,name and  marks) from the user and write onto the binary file.
#The program shouyld be able to get the data from the user and write as long as the user wants.
import pickle
stu={}
with open("stu.dat","wb") as f:
    ans="y"
    while(ans=="y"):
        rno=int(input("Enter the roll number: "))
        name=input("Enter the name: ")
        marks=float(input("Enter your marks: "))
        stu["RollNo"]=rno
        stu["Name"]=name
        stu["Marks"]=marks
        pickle.dump(stu,f)
        ans=input("Wanna add some more input????")
        
