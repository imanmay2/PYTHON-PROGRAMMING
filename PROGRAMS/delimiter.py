import csv
with open("excer.csv","w") as f:
    c=csv.writer(f,delimiter="|")
    li=[
        ["hello","world"],
        ["welcome","to","world"]
    ]
    c.writerows(li)

    