# wap that will generate a random  4 digit number from digits 0-9 and insert the unique numbers serially in the database table.
import random
f=ct=0
li=[]
while True:
    n=random.randint(1000,9999)
    if(n not in li):
        li.append(n)
        f=f+1
    if(f==9000):
        print("PROGRAM TERMINATES...")
        for i in li:
            print(i,end=',')
        break