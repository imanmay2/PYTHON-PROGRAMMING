#1.
import pickle
emp1={"Empno":1201,"Name":"Anushree","Age":25,"Salary":47000}
emp2={"Empno":1211,"Name":"Zoya","Age":30,"Salary":48000}
with open("emp.dat","wb") as f:
    pickle.dump(emp1,f)
    pickle.dump(emp2,f)
    print("File has been successfully added to the .dat extension")
