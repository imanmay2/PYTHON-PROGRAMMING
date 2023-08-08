# WAP that will generate 92 rows and 4 columns
import csv
from datetime import datetime
import random
with open("ludo.csv","w") as f1:
    f=csv.writer(f1)
    f.writerow(["Time1","Low","Time2","Marks"])

    #concept
    now=datetime.now()
    # 2023-06-11 17:49:11.054093
    time=str(now).split('.')[0]
    num='0123456789'
    time1=''
    # for i in time:
    #     if(i in num):
    #         time1=time1+i
    #while(i<=92):
        #l=random.randint(57000,62000)
        #h=random.randint(57000,62000)
        #if(l<h):
        #    print(l,h)
         #   i+=1
    # print(time1)   2023 07 01 20 55 56
    time1=20230612063456
    li=list()
    k=0
    
    time1=int(time1)
    l=[20000,30000,40000]
    for i in range(18):
        r=random.randint(0,2)
        li.append(time1+k+l[r])
        k=k+1000000
        
    time1=20230701233107
    k=0
    l=[20000,30000,40000]
    for i in range(31):
        r=random.randint(0,2)
        li.append(time1+k+l[r])
        k=k+1000000
        
    
    time1=20230801002156
    k=0
    l=[20000,30000,40000]
    for i in range(31):
        r=random.randint(0,2)
        li.append(time1+k+l[r])
        k=k+1000000
        
    time1=202309011624524
    k=0
    l=[20000,30000,40000]
    for i in range(12):
        r=random.randint(0,2)
        k=k+1000000
        li.append(time1+k+l[r])
    j=0
    
    print(len(li))
    li1=[10000,20000,30000,40000]
    while(j<=91):
        l=random.randint(57000,62000)
        h=random.randint(57000,62000)
        if(l<h):
            t1=li[j]
            t2=t1+li1[random.randint(0,3)]
            f.writerow([t1,l,t2,h])
            j+=1

        
