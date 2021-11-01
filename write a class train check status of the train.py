class Train:
    def __init__(self,name,fare,seat):
        self.name=name
        self.fare=fare
        self.seat=seat
    def book(self):
        if(self.seat>0):
            print("**************your booking has been aggreed******************")
            self.seat=self.seat-1
        else:
            print(f"sorry the {self.name} train is full please try any other train")
    def getstatus(self):
        print("name of the train is",self.name)
        print("fare of the train is",self.fare)
        print("seats available of the train is",self.seat)
    
            
        
        

    
Intercity=Train("Intercity",90,1)
Intercity.getstatus()
Intercity.book()
Intercity.getstatus()

        
