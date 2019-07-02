import tkinter as tk
from tkinter.filedialog import *

userGui = Tk()

label1 = Label(userGui, width="20", height="15", bg="red")

label2 = Label(userGui, width="20", height="3", bg="blue")

label1.grid(row=0, column=2)

userGui.mainloop()