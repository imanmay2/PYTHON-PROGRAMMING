age=int(input("enter the age of your employee"))
sal=float(input("enter your salary"))
if(age>39 and age<56):
    bonus=(15.5*sal)/100
    total=bonus+sal
else:
    bonus=(7*sal)/100
    total=bonus+sal
print("The total salary of an employee is",total)

