# wap that will generate a random  4 digit numbers from digits 0-9 and insert the unique numbers serially in the database table.
import mysql.connector as p
from random import shuffle 
import time
t=time.time()
mycon=p.connect(host="localhost",user="root",passwd="25082004",database="hello")
cursor=mycon.cursor()
q1="create table if not exists rand_4_dig(SL_NO int(5),NUMBER int(5))"
cursor.execute(q1)
mycon.commit()


f=0
li=[]
for i in range(1000,9999+1):
    li.append(i)
shuffle(li)
for j in li:
    f+=1
    q2="insert into rand_4_dig values('{}','{}')".format(f,j)
    cursor.execute(q2)
    mycon.commit()
if(f==9000):
    n=time.time()
    print("PROGRAM TERMINATES IN",n,"SECONDS")