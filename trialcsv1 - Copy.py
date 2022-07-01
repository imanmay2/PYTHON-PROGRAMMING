import csv
with open("res2.csv","w") as f:
    wr=csv.writer(f)
    wr.writerows(
        [
            ["Name","Points","Rank"],
            ["Shardha","4500","23"],
            ["Ali","4500","23"]
        ]
    )


with open("res2.csv","r") as k:
    f=csv.reader(k)
    for i in f:
        print(i)
