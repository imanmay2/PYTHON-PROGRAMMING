def append():
    with open(input("ENTER ANY FILE NAME: "),"w") as fj:
        for i in range(int(input("ENTER HOW MANY INPUTS"))):
            name=input("enter the name of the student: ")
            roll=int(input("ENTER THE ROLL NUMBER: "))
            marks=float(input("ENTER THE MARKS OF THE STUDENT: "))
            rec=name,",",+str(roll),','+str(marks)+"\n"
            fj.write(rec)
append()