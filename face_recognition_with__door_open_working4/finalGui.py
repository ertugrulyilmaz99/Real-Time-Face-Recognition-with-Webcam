import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from face_recognition_casper import CasperFaceID
from tkinter import filedialog
from tkinter import messagebox

class gui:
    global userGui
    def start(argv):
        from finalGui import gui

        userGui = Tk()
        userGui.title("Casper Yüz Tanıma Sistemi")

        label1 = Label(userGui, width="35", height="8", bg="blue2")

        addPersonLabel = Label(userGui, width="35", height="12", bg="red")

        detectPersonLabel = Label(userGui, width="35", height="12", bg="green")

        removePersonLabel = Label(userGui, width="35", height="12", bg="orange")

        addPersonButton = Button(userGui, text="Add Person", command=lambda: CasperFaceID().addPerson())

        detectPersonButton = Button(userGui, text="Detect Person", command=lambda: CasperFaceID().detect())

        removePersonButton = Button(userGui, text="Remove Person", command=lambda: gui().wantToRemove())

        withPlus = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\with plus.png")
        addPersonButton.config(image=withPlus, compound=BOTTOM)

        withoutPlusTwo = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\without plus two.png")
        detectPersonButton.config(image=withoutPlusTwo, compound=BOTTOM)

        withRedPlus = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\with red plus.png")
        removePersonButton.config(image=withRedPlus, compound=BOTTOM)

        #casperLogo = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\casper logo.png")
        #label1.config(image=casperLogo)


        addPersonButton.grid(row=1, column=0)
        detectPersonButton.grid(row=1, column=1)
        removePersonButton.grid(row=1, column=2)

        label1.grid(row=0, column=0)
        addPersonLabel.grid(row=1, column=0)
        detectPersonLabel.grid(row=1, column=1)
        removePersonLabel.grid(row=1, column=2)


        userGui.mainloop()

    def wantToRemove(self):
        from finalGui import gui
        answer = filedialog.askdirectory(initialdir=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")

        if not answer:
            messagebox.showinfo("Information", "No one is removed")
        else:
            CasperFaceID().remove(answer)



if __name__ == "__main__":
   gui.start(sys.argv[1:])