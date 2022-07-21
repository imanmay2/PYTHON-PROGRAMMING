import tkinter
def wquit():
    print("Hello! Tkinter")
root=tkinter.Tk()
w1=tkinter.Label(root,text="Hello there")
w1.pack()
w2=tkinter.Button(root,text="Hello there",command=wquit)
w2.pack()
root.mainloop()
