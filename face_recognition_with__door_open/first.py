import tkinter as tk
import sys, getopt, os
from tkinter.filedialog import *
from PIL import Image, ImageTk

from face_recognition_casper import CasperFaceID


#CasperFaceID().addPerson(0)



nRow = None
nCol = None

userGui = tk.Tk()
xSize, ySize = 675, 1100
size = str(ySize) + "x" + str(xSize)
userGui.geometry(size)
userGui.title("PASS - LOCK")
userGui.configure(bg="deep sky blue")


#for r in range(2):
 #   for c in range(2):
  #      if r == 0:
   #         Label(userGui)



for r in range(2):
    for c in range(2):
        if r == 0:
            Label(userGui, bg='red').grid(row=r, column=c, padx=(xSize / 6) - 15, pady=20)
        else:
            Label(userGui, bg='blue', text="test").grid(row=r, column=c, padx=0, pady=(ySize * 2 / 8))



addPersonButton = Button(userGui, text='Binary', borderwidth=1, relief=RAISED)
addPersonButton.grid(row=0, column=1, sticky=NE, padx=20, pady=20)

#addPersonButton.pack()
userGui.mainloop()







#if __name__ == "__main__":
 #  main(sys.argv[1:])

