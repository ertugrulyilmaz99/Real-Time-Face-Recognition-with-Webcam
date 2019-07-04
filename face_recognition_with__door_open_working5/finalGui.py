import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from face_recognition_casper import CasperFaceID
from tkinter import filedialog
from tkinter import messagebox

class gui:

    # Main GUI Method
    def start(argv):
        # Declaring GUI variable
        userGui = tk.Tk()
        # Initializing borders
        xSize , ySize = 355, 600
        # Store them in one variable
        size = str(ySize) + "x" + str(xSize)
        # Initialize it to GUI
        userGui.geometry(size)
        # Initialize a title for GUI
        userGui.title("Casper Yüz Tanıma Sistemi")
        # Whıle window color
        userGui.configure(bg="white")
        # Initializing template which is 2x1
        for r in range(2):
            for c in range(1):
                if r == 1:
                    Label(userGui, bg='red').grid(row=r, column=c, padx=300, pady=0)
                else:
                    Label(userGui, bg='blue').grid(row=r, column=c, padx=300, pady=0)
        # Declaring and initializing label which is going to store casper variable
        casperLabel = Label(userGui)
        # Declaring and initializing add person button
        addPersonButton = Button(userGui, text="Add Person", command=lambda: CasperFaceID().addPerson(), bg="blue2",font="STIXGeneral")
        # Declaring and initializing detect person button
        detectPersonButton = Button(userGui, text="Detect Person", command=lambda: CasperFaceID().detect(), bg="blue2",font="STIXGeneral")
        # Declaring and initializing remove person button
        removePersonButton = Button(userGui, text="Remove Person", command=lambda: gui().wantToRemove(), bg="blue2",font="STIXGeneral")
        # Initializing icon for buttons and initialize it to button
        withPlus = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\with plus.png")
        addPersonButton.config(image=withPlus, compound=BOTTOM)
        # Initializing icon for buttons and initialize it to button
        withoutPlusTwo = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\without plus two.png")
        detectPersonButton.config(image=withoutPlusTwo, compound=BOTTOM)
        # Initializing icon for buttons and initialize it to button
        withRedPlus = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\with red plus.png")
        removePersonButton.config(image=withRedPlus, compound=BOTTOM)
        # Initializing icon for buttons and initialize it to button
        casperLogo = PhotoImage(file=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\button icons\casper_logo.png")
        casperLabel.config(image=casperLogo, compound=BOTTOM)
        # Place them to their locations
        casperLabel.grid(row=0, column=0)
        addPersonButton.grid(row=1, column=0, sticky='W')
        detectPersonButton.grid(row=1, column=0)
        removePersonButton.grid(row=1, column=0, sticky='E')
        # Maimloop for GUI
        userGui.mainloop()

    # A method which takes file path from user as input
    def wantToRemove(self):
        # Store the users answer who is going to remove
        answer = filedialog.askdirectory(initialdir=r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")
        # If user presses cancel button
        if not answer:
            messagebox.showinfo("Information", "No one is removed")
        # If user selects a folder
        else:
            # Just store the name of that file
            name = answer.split("/")[6]
            # Ask to user one more time
            yesNo = messagebox.askyesno("Warning!", "Are you going to delete '" + name + "' ?")
            # If user presses yes remove the person from database
            if yesNo:
                CasperFaceID().remove(answer)
            # If user presses no nothing happens
            else:
                messagebox.showinfo("Information", "No one is removed")

if __name__ == "__main__":
    gui.start(sys.argv[1:])
