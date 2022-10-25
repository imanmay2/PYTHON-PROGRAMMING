# Q1) Make a GUI application which ask user to enter messaages that store in your local db
# store in encrypted version.
# 

# if u wanna go a bit level then make the button in such a way that when the
# message is of less than 10 characters then  the button will be grey color and non-functional
# and if the character exceeds 10 then the button changes to green and become functional.


from tkinter import *
from tkinter import messagebox
from xer import deci_hexa as e 
import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='2%0*2)0$Happy',database='hello')
cursor=mycon.cursor()
cursor.execute("create table if not exists tkinter (encrypted longtext)") 
win=Tk()
win.title("XCHAT")
def func():
    l=list()
    li=list()
    str3=''
    str1=var.get()
    if(len(str1)<=10):
        messagebox.showerror("error","PLEASE!! ENTER MORE THAN 10 CHARACTERS TO PROCEED!!")
    else:
        for i in str1:
            l.append(ord(i))
        for j in l:
            li.append(e(j))
        for k in li:
            str3+=k
        messagebox.showinfo("success",str3)
        cursor.execute("insert into tkinter values('{}');".format(str3))
        mycon.commit()
        
var=StringVar()
win.maxsize(width=600,height=250)
win.minsize(width=600,height=250)
Label(win,text="WELCOME TO THE WORLD OF XCHAT",bg='red',fg="white").pack()
Label(win,text="UPLOAD",bg='GREEN',fg="white",height=2).place(x=0,y=50)
Entry(win,bd=5,font='arial',text='UPLOAD',width=40,fg='black',textvariable=var).place(x=80,y=50)
Button(win,text='LOG IN',bg='yellow',command=func,width=5,height=3).place(x=250,y=100)
win.mainloop()
