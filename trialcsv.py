import csv
with open("delimiter.csv","w") as f3:
    deli=csv.writer(f3,d)
    deli.writerow(["Name","Points","Rank"])