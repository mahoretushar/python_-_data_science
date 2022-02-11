from tkinter import *

root = Tk()

entry_1 = Entry(root, width=50, borderwidth=10)
entry_1.pack()


def button_click():
    greet = "Hello " + entry_1.get()
    label_1 = Label(root, text=greet)
    label_1.pack()


button_1 = Button(root, text="Click Here", padx=50, command=button_click)
button_1.pack()

root.mainloop()
