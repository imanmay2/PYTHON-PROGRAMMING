from tkinter import *
win=Tk()
lst=Listbox(win,width=27,bg='yellow')
items=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,0]
for i in items:
    lst.insert(END,i)
lst.pack()
