class employee:
    company="MICROSOFT"
    def empDetails(self):
        print(f"{self.name} working under {self.company} age {self.age} getting salary {self.salary}")
emp=employee()
emp2=employee()
emp.name=input("Enter your name")
emp.salary=int(input("Enter your salary"))
emp.age=int(input("Enter your age"))
employee.company="GOOGLE"
emp2.name=input("Enter your name")
emp2.salary=int(input("Enter your salary"))
emp2.age=int(input("Enter your age"))
emp.empDetails()
emp2.empDetails()
