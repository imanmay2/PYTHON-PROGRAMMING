import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='2%0*2)0$Happy',database='hello')
cursor=mycon.cursor()
cursor.execute("select * from tkinter")
data=cursor.fetchall()  
items=list()
for i in data:
    items.append(i[0])
print(type(items))
