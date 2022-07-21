import mysql.connector
from random import shuffle   #optional
import time
start=time.time()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="25082004",
  database="hello"
)
mycursor = mydb.cursor()
if mydb:
    query="create table if not exists Chlgn2(Slno int(4) primary key AUTO_INCREMENT,Num int(4));"
    mycursor.execute(query)
    numList=[]
    for i in range(1000,10000):
        numList.append(i)
    shuffle(numList)   #optional
    for i in numList:
        query=f"insert into Chlgn2(Num) values({i})"
        mycursor.execute(query)
        mydb.commit()
    end=time.time()
    print(f"PROGRAMS TERMINATES AFTER {end-start} SECONDS")
else:
    print("Failed to connect. Try again later")
