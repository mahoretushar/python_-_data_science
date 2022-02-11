from tkinter import *

root = Tk()


def button_click():
    label_1 = Label(root, text="Hello World")
    label_1.pack()


button_1 = Button(root, text="Click Here", padx=50, command=button_click, fg="green", bg="blue")

button_1.pack()

root.mainloop()
