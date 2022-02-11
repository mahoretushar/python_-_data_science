from tkinter import *

root = Tk()

# creating a label
label_1 = Label(root, text="Hello World")
label_2 = Label(root, text="I am Batman")
label_3 = Label(root, text="Batman vs Superman")

# putting up on screen
label_1.grid(row=0, column=0)
label_2.grid(row=0, column=5)
label_3.grid(row=1, column=1)

root.mainloop()
