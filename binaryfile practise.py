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