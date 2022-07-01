class RailForm:
    def info(self):
        print(f"Passenger's name is {self.name} going in train {self.train} to {self.desti}")
harry=RailForm()
harry.name=input("Enter your name please")
harry.train=input("Enter your trains name")
harry.desti=input("Please enter your destination")
harry.info()
