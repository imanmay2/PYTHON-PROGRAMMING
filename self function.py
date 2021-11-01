class emp:
    company="Microsoft"
    def getsalary(self):
        print(f"The salary of the employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning your salary has been deposited to your respective account no.")
harry=emp()
harry.salary="100000"
harry.getsalary()
harry.greet()
