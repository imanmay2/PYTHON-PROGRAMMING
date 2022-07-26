import tkinter as t
root=t.Tk()
root.title("WELCOME!!")
q=t.Entry(root).pack()
print("TEXT ENTERED IN THE TK WINDOW IS: ",q.get())
root.mainloop()
