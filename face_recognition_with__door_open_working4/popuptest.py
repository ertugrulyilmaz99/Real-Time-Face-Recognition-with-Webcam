import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from face_recognition_casper import CasperFaceID
from tkinter import filedialog
from tkinter import messagebox

userGui =Tk()

#answer = filedialog.askdirectory(parent=userGui,initialdir=os.getcwd())
answer = filedialog.askdirectory(parent=userGui,initialdir=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")
#answer1 = messagebox.askokcancel("Question","Do you want to open this file?")
#answer2 = messagebox.askretrycancel("Question", "Do you want to try that again?")
#answer3 = messagebox.askyesno("Question","Do you like Python?")
#answer4 = messagebox.askyesnocancel("Question", "Continue playing?")
messagebox.showinfo("Information", "No one is removed")
print(answer)
if not answer:
    print("tamam")
#print(answer1)
#print(answer2)
#print(answer3)
#print(answer4)
userGui.mainloop()

