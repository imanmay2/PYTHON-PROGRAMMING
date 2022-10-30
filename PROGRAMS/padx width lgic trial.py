from tkinter import *
win=Tk()
win.minsize(width=400,height=700)
win.config(background='Grey')
li_alpha=['MMMMMM','hhhhhh','LLLLLL','llllll','oooooo','WWWWWW','OOOOOO','AAAAAA']
TEMP=0
for i in range(1,17):
    if TEMP==8:
        TEMP=0
    lbl=Label(win,text=li_alpha[TEMP],bg='yellow',fg='black',width=9)
    lbl.pack(padx=360,pady=3)
    TEMP+=1
win.mainloop()
