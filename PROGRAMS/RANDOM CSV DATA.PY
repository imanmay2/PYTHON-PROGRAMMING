import csv
import random
with open("Test.csv","w") as f:
    s=csv.writer(f)
    s.writerow(['Airport_Name','Flights_Available','Passengers','Going to','Cost of tickets'])
    n=int(input("ENTER THE NUMBER OF CASES: "))
    ct=0
    li_Airport=["AMSTERDAM","FRANKFURT","HALLEY","NETHERLANDS","SILICON VALLEY","MEXICO","HAMEBURG","MUMBAI","DELHI","KOLKATA","KOTA","BIHAR"]    
    while True:
        ct+=1
        if(ct==n):
            break
        else:
            _1=li_Airport[random.randint(0,11)]
            _2=li_Airport[random.randint(0,11)]
            if(_1!=_2):
                s.writerow([_1,random.randint(0,8),random.randint(800,1600),_2,random.randint(35000,100000)])
            elif(_1==_2):
                ct=ct-1
                


        
    
    
