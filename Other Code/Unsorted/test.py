# File: protocol1.py

import tkinter
from tkinter import messagebox

def callback():
 MsgBox = tkMessageBox.askokcancel("Quit", "Do you really wish to quit?")
 if MsgBox:
    root.destroy()

    root = Tk()
    root.protocol("WM_DELETE_WINDOW", callback)

    root.mainloop()
