#P OS V0.1,DO NOT USE CODE COMMERCIALLY OR USE THIS CODE WITHOUT CREDIT TO ORIGINAL OWNER OF P OS, P OS IS ALL ASSETS OF PHONEZ 2020 AND BEYOND
#IMPORTS
from tkinter import *
from tkinter import messagebox
import tkinter as tk
root = tk.Tk()
root.withdraw()
import time
import random
import sys
#IMPORTS
#VARIABLES
loadpercent1 = 0
selcdirec = ""
#VARIABLES

#APPFUNCTIONS
def CALC():
    print("wip")
#APPFUNCTIONS
#DIRECTORYINPUTS
def LOAD():
    global loadpercent1
    print("P OS V0.1 LOADING")
    while loadpercent1 < 100:

        time.sleep(0.5)
        loadpercent1 = loadpercent1 + random.randint(5,10)
        if loadpercent1 > 100:
            loadpercent1 = 100
        print ("P OS IS: " + str(loadpercent1) + " PERCENT LOADED")
    print("P OS Has Loaded")
    print("Press H For Help")
    MENU()
def INVALID():
    print("Invalid Option")
def INVALIDMENU():
    print("Invalid Option")
    MENU()
def COMPUTER():
    global selcdirec
    selcdirec = selcdirec + "computer"
    print("directory: " + selcdirec)
    direcinput = input("Input Directory:")
    if direcinput == "applications":
        APPLICATIONS()
    else:
        INVALID()
def APPLICATIONS():
    global selcdirec
    selcdirec = selcdirec + "/applications"
    print("directory: " + selcdirec)
    direcinput = input("Input Directory:")
    if direcinput == "calculator":
        CALCULATOR()
    else:
        INVALID()
def CALCULATOR():
    global selcdirec
    selcdirec = selcdirec + "/calculator"
    print("directory: " + selcdirec)
    direcinput = input("Do You Want To Run " + selcdirec + " Y or N")
def MENU():
    KEYINPUT = input("Select What You Want To Do")
    if KEYINPUT == "i":
        INPUTDIREC()
    elif KEYINPUT == "r":
        print("P OS Shutting Down")
        sys.exit()
    elif KEYINPUT == "h":
        print("Help Selected")
        pgselc = input("What Page Do You Want To Select, Input R To Quit")
        if pgselc == "1":
            print("To Select A Directory,Input I ,When You Want To Logg Off P OS,Input R")
            print("P Help V.01")
            time.sleep(3)
            MENU()
    else:
        INVALIDMENU()
#DIRECTORYINPUTS
#DIRECTORYDETECTORS
def INPUTDIREC():
    direcinput = input("Input Directory:")
    if direcinput == "computer":
        COMPUTER()
    else:
        INVALID()
#DIRECTORYDETECTORS
#LOADING CODE
LOAD()