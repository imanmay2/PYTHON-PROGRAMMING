class programmer:
    company="Microsoft"
    def __init__(self,name,address,phone_number):
        self.name=name
        self.address=address
        self.phone_number=phone_number
    def getdetails(self):
        print(f"Name of the employee working under {self.company} is {self.name} , address is {self.address} and phone number is {self.phone_number}")
harry=programmer("harry","Mumbai",7001552252)
manmay=programmer("Manmay","kaliyaganj",7478333867)
software=programmer("Software Engineer","USA",98764532)
harry.getdetails()
manmay.getdetails()
software.getdetails()


        
