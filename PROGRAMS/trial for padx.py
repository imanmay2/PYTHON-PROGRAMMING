from tkinter import *
window = Tk()
window.minsize(width=100,height=100)
window.maxsize(width=100,height=100)
my_text_label = Label(window, text='This is some text', width=18, height=4, bg='yellow')
my_text_label.pack(padx=1000, pady=10)

window.mainloop()
