import tkinter as tk
from tkinter.filedialog import *
from face_recognition_casper import CasperFaceID
from asdfghjk import witht
class main:

    def start(argv):
        nRow = None
        nCol = None

        userGui = tk.Tk()
        xSize, ySize = 300, 0
        size = str(ySize) + "x" + str(xSize)
        userGui.geometry(size)
        userGui.title("PASS - LOCK")
        userGui.configure(bg="deep sky blue")


        for r in range(3):
            for c in range(1):
                if r == 0:
                    Label(userGui, bg='red').grid(row=r, column=c, padx=0, pady=0)
                else:
                    Label(userGui, bg='blue', text="test").grid(row=r, column=c, padx=0, pady=0)


        addPersonButton = Button(userGui, text='Add Person', command= lambda :CasperFaceID().addPerson(), borderwidth=1, relief=RAISED)
        addPersonButton.grid(row=1, column=0, sticky='', padx=0, pady=0)

        #detectPersonButton = Button(userGui, text="Detect Person", command=lambda: witht().test1())
        detectPersonButton = Button(userGui,text="Detect Person", command = lambda : CasperFaceID().detect())
        detectPersonButton.grid(row=2, column=0, sticky='N', padx=0, pady=0)
        userGui.mainloop()


if __name__ == "__main__":
   main.start(sys.argv[1:])
