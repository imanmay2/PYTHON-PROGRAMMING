from tkinter import *
from tkinter import messagebox
from SLS_ALGO import encrypt as e
win=Tk()
def func():
    pas=var.get()
    messagebox.showinfo("SUCCESS",e(pas))
var=StringVar()
win.title("XCHAT")
win.maxsize(width=600,height=250)
win.minsize(width=600,height=250)
Label(win,text="WELCOME TO THE WORLD OF XCHAT",bg='red',fg="white").pack()
Label(win,text="USERNAME",bg='GREEN',fg="white",height=2).place(x=0,y=50)
Entry(win,bd=5,font='arial',text='USERNAME',width=40,fg='black').place(x=80,y=50)
Label(win,text="PASSWORD",bg='GREEN',fg="white",height=2).place(x=0,y=100)
Entry(win,bd=5,font='arial',text='PASSWORD',width=40,textvariable=var).place(x=80,y=100)
Button(win,text='LOG IN',bg='yellow',command=func,width=5,height=3).place(x=250,y=160)
win.mainloop()



