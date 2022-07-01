# employee nested dictionary.
emp={"John":{"age":25,"salary":20000},"Diya":{"age":36,"salary":360000}}
for i in emp:
    print("employee",i)
    print("Age",emp[i]["age"])
    print("Salary",emp[i]["salary"])
