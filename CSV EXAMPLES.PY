#wap that will accept records of 5 students from the user and write that records in the stu.csv file
import csv
with open("stu.csv","w") as f1:
    f=csv.writer(f1)
    f.writerow(["Roll_No","Name","Marks"])
    for i in range(1,6):
        print("Enter record no.",i)
        r=int(input("Enter the Roll No. of the student: "))
        n=input("Enter the Name of the student: ")
        m=float(input("Enter the marks of the student: "))
        f.writerow([r,n,m])
    
#Using the function of writerows()
with open("result.csv","w") as f:
    wr=csv.writer(f)
    wr.writerows(
        [
            ["Name","Points","Rank"]
            ["Shradha","4500","23"]
            ["Nischay","4800","31"]
            ["Ali","4500","25"]
            ["Adi","5100","14"]
        ]
    )