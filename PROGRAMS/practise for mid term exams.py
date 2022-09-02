import csv
with open("mid.csv","r") as f:
    for i in csv.reader(f,delimiter="|"):
        print(i)
    

    
    
