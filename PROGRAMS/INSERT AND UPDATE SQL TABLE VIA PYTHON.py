import mysql.connector as p
mycon=p.connect(host="localhost",user="root",passwd="25082004",database="hello")
cursor=mycon.cursor()
q="insert into todo values('{}','{}','{}','{}','{}','{}')".format("hello","world","of","pro","gram","ing")
cursor.execute(q)
mycon.commit()

q1="update todo set TASK_TITLE='{}'".format(" ")
cursor.execute(q1)
mycon.commit()

q2="drop table todo"
cursor.execute(q2)
mycon.commit()



