#wap accept salary and age of an emplyee if age of an employee
#is 40 to 55 then he gets 15.5% bonus of
#the salary otherwise he gets 7% bonus of that salary
#then dispaly the total salary of an emplyee.
age=int(input("enter the age of your employee"))
sal=float(input("enter your salary"))
if(age>39 and age<56):
    bonus=0.15*sal
    total=bonus+sal
else:
    bonus=0.07*sal
    total=bonus+salary
print("The total salary of an employee is",total)

