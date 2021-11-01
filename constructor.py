                                ####BY USING CONSTRUCTOR FUNCTION######



class employee:
    def __init__(self,name,salary,subunit):
        print("Employee's detailes is created")
        self.name=name
        self.salary=salary
        self.subunit=subunit
    def getdetails(self):
        print(f"the name of the employye is {self.name} , subunit is {self.subunit} and salary is {self.salary}")
harry=employee("Manmay",100000,"Microsoft")
harry.getdetails()
    
