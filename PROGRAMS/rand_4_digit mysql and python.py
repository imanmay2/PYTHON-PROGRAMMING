# wap that will generate a random  4 digit numbers from digits 0-9 and insert the unique numbers serially in the database table.
import mysql.connector as p
import random
mycon=p.connect(host="localhost",user="root",passwd="25082004",database="hello")
cursor=mycon.cursor()
q1="create table rand_4_dig(SL_NO int(5),NUMBER int(5))"
cursor.execute(q1)
mycon.commit()


f=ct=0
li=[]
while True:
    n=random.randint(1000,9999)
    if(n not in li):
        f=f+1
        q2="insert into rand_4_dig values('{}','{}')".format(f,n)
        cursor.execute(q2)
        mycon.commit()
    if(f==9000):
        print("PROGRAM TERMINATES...")

