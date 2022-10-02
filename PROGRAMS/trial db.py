import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="2%0*2)0$Happy",database="project")
cursor=mycon.cursor()
cursor.execute("select * from {}".format("2xii"))
data=cursor.fetchall()
for i in data:
    for j in i:
        print(j)


