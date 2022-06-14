import csv
with open("result.csv","w") as f:
    wr=csv.writer(f)
    wr.writerows(
        [
            ["Name","Points","Rank"],
            ["Shradha",4500,23],
            ["Nischay",4800,31],
            ["Ali",4500,25],
            ["Adi",5100,14]
        ]
    )