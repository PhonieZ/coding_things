import tkinter
import time
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

messagebox.showwarning("WARNING","I Diagnose Your Computer With DEAD")
time.sleep(1)
import os
while True:
       def openNewWindow():
        firstWindow.destroy()


       secondWindow = root
       secondWindow.title("Second Window")

       photoTwo = PhotoImage(file="freedom.gif")
       labelTwo = Label(secondWindow, image=photoTwo).pack()

       secondWindow.mainloop()



firstWindow = Tk()


firstWindow.title("First Window")

logo = PhotoImage(file="burger.gif")
w1 = Label(firstWindow, image=logo).pack()

closeBttn = Button(firstWindow, text="Close!", command=openNewWindow)
closeBttn.pack()

firstWindow.mainloop()