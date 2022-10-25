#Q2) Make another application which fetches all the data from the db and
# display it's decypted form.
from tkinter import * 
import mysql.connector as con
mycon=con.connect(host='localhost',user='root',passwd='2%0*2)0$Happy',database='hello')
cursor=mycon.cursor()
def access():
    cursor.execute("select * from tkinter")
    data=cursor.fetchall()  
    items=list()
    for i in data:
        items.append(i[0])
    return items 
def hexa_deci_char(num):
    #hexadecimal to decimal
    li2=grp(num)
    li3=list()
    for i in li2:
        li3.append(int(i,16)) # shortcut to be changed later...change this
    str4=''
    for i in li3:
        str4+=chr(i)
    return str4  
        
def grp(num):
    str1=''
    ct=0
    li=list()
    for i in num:
        str1+=i
        ct=ct+1
        if(ct==2):
            li.append(str1)
            str1=''
            ct=0
    return li
def func():
    for i in access():
        lst.insert(END,hexa_deci_char(i))    
win=Tk()
var=StringVar()
win.maxsize(width=600,height=250)
win.minsize(width=600,height=250)
Label(win,text="WELCOME TO THE WORLD OF DECRYPTOR",bg='red',fg="white").pack()
lst=Listbox(win,width=27)
Button(win,text='PRESS TO DECRYPT',bg='yellow',command=func,width=15,height=3).place(x=250,y=50)
lst.place(x=225,y=120)
win.mainloop()
