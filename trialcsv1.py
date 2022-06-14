import csv
with open("res1.csv","w",newline="\r\n") as f:
    wr=csv.writer(f)
    wr.writerows(
        [
            ["Name","Points","Rank"],
            ["Shardha","4500","23"],
            ["Ali","4500","23"]
        ]
    )