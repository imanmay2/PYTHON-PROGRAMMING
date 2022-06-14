import csv
with open("result.csv","r") as f4:
    t=csv.reader(f4)
    for i in t:
        print(i)