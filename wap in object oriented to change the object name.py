class Emp:
    company="Google"
    comp="YouTube"
    salary="4000"
manmay=Emp()
lopa=Emp()
print(manmay.company,lopa.comp)
Emp.company="Microsoft"
Emp.comp="lol"
manmay.salary="300"
#lopa.salary="400"
print(manmay.company,lopa.comp)
print(manmay.salary,lopa.salary)
