#-------------------------------------------------------------------------------
# Name:         CrypticBoot
# Purpose:
#
# Author:      m.aydin
#
# Created:     06/02/2020
# Copyright:   (c) PhoneZ 2020
# Licence:     Do Not Copy Or Modify
#-------------------------------------------------------------------------------



#imports
from tkinter import *
from tkinter import messagebox
import tkinter
root = tkinter.Tk()
root.withdraw()
import random
import signal
#imports



#main

top = Tk()
top.geometry("250x200")
def Timer():
    root = Tk()
    timee = Text(root)
    timee.insert(INSERT, "Time Left:" + signal.alarm.timeout )
    timee.pack()
def Noob():
    q
def Easy():
    q


def Normal():
    print("yes")
    tim = 0
    d1 = random.randint(1,30)
    d2 = random.randint(1,30)
    d3 = random.randint(1,30)
    d4 = random.randint(1,30)
    done1 = 1
    signal.alarm.timeout(60)
    try:


        while done1 == 1:

            ans = input("Input Key:")
            if ans == str(d1):
                messagebox.showinfo("CrypticBoot","Success,Layer 1 Decoded" )
                done1=2
            else:
                messagebox.showinfo("CrypticBoot","Incorrect,Retry" )
                done1= 1
        done2= 1
        while done2 == 1:

            ans = input("Input Key:")
            if ans == str(d2):
                messagebox.showinfo("CrypticBoot","Success,Layer 2 Decoded" )
                done2=2
            else:
                messagebox.showinfo("CrypticBoot","Incorrect,Retry" )
                done2= 1
        done4= 1
        while done4 == 1:
            ans = input("Input Key:")
            if ans == str(d3):
                messagebox.showinfo("CrypticBoot","Success,Layer 3 Decoded" )
                done4=2
            else:
                messagebox.showinfo("CrypticBoot","Incorrect,Retry" )
                done4= 1
        done3= 1
        while done3 == 1:
            ans = input("Input Key:")
            if ans == str(d4):
                messagebox.showinfo("CrypticBoot","Success,All Layers Decoded" )
                Main()
                done3=2
            else:
                messagebox.showinfo("CrypticBoot","Incorrect,Retry" )
                done3= 1
    except:
         messagebox.showinfo("CrypticBoot","Error:Time == 0, Please Reboot" )
         # print score
def Hard():
    q
def Quit():
    msgbox = messagebox.askquestion("CrypticBoot","Are You Sure You Want To Quit")
    if msgbox == 'yes':
        messagebox.showinfo("CrypticBoot","You May Quit Now" )
    else:
        messagebox.showinfo("rypticBoot","Opening...")
        main()


def Main():
    B = Button(top, text = "Noob Mode", command = Noob)
    B.place(x = 0,y = 50)
    B = Button(top, text = "Easy Mode", command = Easy)
    B.place(x = 80,y = 50)
    B = Button(top, text = "Normal Mode", command = Normal)
    B.place(x = 160,y = 50)
    B = Button(top, text = "Hard Mode", command = Hard)
    B.place(x = 0,y = 100)
    B = Button(top, text = "Quit", command = Quit)
    B.place(x = 80,y = 100)
    top.mainloop()
Main()



