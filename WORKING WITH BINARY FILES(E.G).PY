#program to to a binary file called emp.dat and write into it the employee details of some employees, avilable in the form of dictionaries.
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

