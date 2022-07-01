# wap to create a dictionary of two employees along with age and salary..
emp={"Manmay":{"age":24,"salary":250000},"Kartika":{"age":89,"salary":2500000}}
for key in emp:
    print("Employee",key,":")
    print("Age is ",str(emp[key]["age"]))
    print("Salary is",str(emp[key]["salary"]))
