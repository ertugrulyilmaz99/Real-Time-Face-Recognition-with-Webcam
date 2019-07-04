import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from face_recognition_casper import CasperFaceID
from tkinter import filedialog
from tkinter import messagebox

class gui:
    global userGui
    def start(argv):
        from finalGuiOld import gui

        userGui = Tk()
        userGui.title("Casper Yüz Tanıma Sistemi")

        label1 = Label(userGui, width="35", height="8", bg="black")

        label2 = Label(userGui, width="35", height="8", bg="black")

        label3 = Label(userGui, width="35", height="8", bg="black")

        addPersonLabel = Label(userGui, width="35", height="12", bg="black")

        detectPersonLabel = Label(userGui, width="35", height="12", bg="black")

        removePersonLabel = Label(userGui, width="35", height="12", bg="black")

        addPersonButton = Button(userGui, text="Add Person", command=lambda: CasperFaceID().addPerson(), bg="blue2", font="STIXGeneral")

        detectPersonButton = Button(userGui, text="Detect Person", command=lambda: CasperFaceID().detect(), bg="blue2", font="STIXGeneral")

        removePersonButton = Button(userGui, text="Remove Person", command=lambda: gui().wantToRemove(), bg="blue2", font="STIXGeneral")

        withPlus = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\with plus.png")
        addPersonButton.config(image=withPlus, compound=BOTTOM)

        withoutPlusTwo = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\without plus two.png")
        detectPersonButton.config(image=withoutPlusTwo, compound=BOTTOM)

        withRedPlus = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\with red plus.png")
        removePersonButton.config(image=withRedPlus, compound=BOTTOM)

        casperLogo = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\casper logo.png")
        label1.config(image=casperLogo,compound=CENTER)


        addPersonButton.grid(row=1, column=0)
        detectPersonButton.grid(row=1, column=1)
        removePersonButton.grid(row=1, column=2)

        label1.grid(row=0, column=0)
        label2.grid(row=0, column=1)
        label3.grid(row=0, column=2)
        addPersonLabel.grid(row=1, column=0)
        detectPersonLabel.grid(row=1, column=1)
        removePersonLabel.grid(row=1, column=2)


        userGui.mainloop()

    def wantToRemove(self):

        answer = filedialog.askdirectory(initialdir=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")
        if not answer:
            messagebox.showinfo("Information", "No one is removed")
        else:
            name = answer.split("/")[6]
            yesNo = messagebox.askyesno("Warning!", "Are you going to delete '"+name+"' ?")
            if yesNo:
                CasperFaceID().remove(answer)
            else:
                messagebox.showinfo("Information", "No one is removed")


if __name__ == "__main__":
   gui.start(sys.argv[1:])