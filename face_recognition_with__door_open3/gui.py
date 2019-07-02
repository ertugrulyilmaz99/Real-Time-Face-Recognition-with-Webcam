import tkinter as tk
from face_recognition_casper import CasperFaceID

#from tkinter.filedialog import *
import sys

class user:
    def pir(self):
        print("a")

    def start(argv):
        userGui  = tk.Tk()

        userGui.title("Casper Face Recognition")

        tk.Label(userGui,text="Lock - Pass").pack()
        tk.Button(userGui,text="Add Person", command=lambda: CasperFaceID().addPerson()).pack()
        tk.Button(userGui, text="Detect Person", command=lambda: CasperFaceID().detect()).pack()

        userGui.mainloop()

if __name__ == "__main__":
   user.start(sys.argv[1:])


