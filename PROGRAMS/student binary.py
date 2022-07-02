import pickle 
with open("PROGRAMS/student.dat","wb") as f:
    stu=dict()
    for i in range(int(input("Enter the range: "))):
        name=input("Enter the name of the student: ")
        roll=int(input("Enter the roll number of the student: "))
        per=float(input("Enter the percentage of the student: "))
        stu={"Name":name,"Roll":roll,"Percentage":per}
        pickle.dump(stu)

