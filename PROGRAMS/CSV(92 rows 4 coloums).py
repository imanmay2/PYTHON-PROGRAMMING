# WAP that will generate 92 rows and 4 columns
import csv
from datetime import datetime
import random
with open("data.csv","w") as f1:
    f=csv.writer(f1)
    f.writerow(["Time1","Low","Time2","Marks"])

    #concept
    now=datetime.now()
    # 2023-06-11 17:49:11.054093
    time=str(now).split('.')[0]
    num='0123456789'
    time1=''
    for i in time:
        if(i in num):
            time1=time1+i
    i=1
    #while(i<=92):
        #l=random.randint(57000,62000)
        #h=random.randint(57000,62000)
        #if(l<h):
        #    print(l,h)
         #   i+=1
    # print(time1)   2023 07 01 18 47 57
    li=list()
    k=1000000
    time1=int(time1)
    for i in range(18):
        k=k+1000000
        li.append(time1+k)
    time1=20230701184757
    k=1000000
    for i in range(29):
        k=k+1000000
        li.append(time1+k)
    time1=20230801184757
    k=1000000
    for i in range(29):
        k=k+1000000
        li.append(time1+k)
    time1=20230901184757
    k=1000000
    for i in range(16):
        k=k+1000000
        li.append(time1+k)
    j=0
    while(j<=91):
        l=random.randint(57000,62000)
        h=random.randint(57000,62000)
        if(l<h):
            t1=li[j]
            t2=t1+random.randint(10000,40000)
            f.writerow([t1,l,t2,h])
            j+=1

        
