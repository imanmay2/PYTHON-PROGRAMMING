import mysql.connector as p
mycon=p.connect(host="localhost",user="root",passwd="25082004",database="hello")
if mycon.is_connected():
    print("CONNECTION DONE SUCCESSFULLY")
cursor=mycon.cursor()
q="select * from sports where Grade1='{}'".format("B",)
cursor.execute(q)
data=cursor.fetchall()
print(cursor.rowcount)
for i in data:
    print(i)










