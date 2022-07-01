import csv
with open("result.csv","r",newline="\r\n") as rh:
    oh=csv.reader(rh)
    for i in oh:
        print(i)
        with open("excer.csv","w") as jk:
            kgf=csv.writer(jk)
            kgf.writerow(i)
    
        

