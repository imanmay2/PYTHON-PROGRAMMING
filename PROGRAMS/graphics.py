from tkinter import *
import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='2%0*2)0$Happy',database='hello')
cursor=mycon.cursor()
cursor.execute("select * from tkinter")
win=Tk()
win.title("XCHAT")
win.minsize(width=400,height=700)
win.maxsize(width=400,height=700)
Label(height=5,width=66,bg='green').pack()
Listbox(win,height=36,width=66,bg='yellow').place(x=0,y=80)
Text(win,bd=8,height=2,width=43).place(x=0,y=654)
Button(win,text='SEND',height=2,width=4,bg='green',fg='white').place(x=360,y=658)
win.mainloop()
