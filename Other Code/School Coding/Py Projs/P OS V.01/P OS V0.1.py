#P OS V0.1,DO NOT USE CODE COMMERCIALLY OR USE THIS CODE WITHOUT CREDIT TO ORIGINAL OWNER OF P OS, P OS IS ALL ASSETS OF PHONEZ 2020 AND BEYOND
#IMPORTS
import time
import random
import sys
#IMPORTS
#VARIABLES
loadpercent1 = 0
selcdirec = ""
#VARIABLES

#APPFUNCTIONS

#APPFUNCTIONS
#DIRECTORYINPUTS
def COMPUTER():
    global selcdirec
    selcdirec = selcdirec + "computer"
    print("directory: " + selcdirec)
    direcinput = input("Input Directory:")
def APLLICATIONS():
    global selcdirec
    selcdirec = selcdirec + "/applications"
    print("directory: " + selcdirec)
    direcinput = input("Input Directory:")
def CALCULATOR():
    global selcdirec
    selcdirec = selcdirec + "/calculator"
    print("directory: " + selcdirec)
    direcinput = input("Do You Want To Run" + selcdirec + "Y or N")

#DIRECTORYINPUTS
#DIRECTORYDETECTORS
def INPUTDIREC():
    direcinput = input("Input Directory:")
    if direcinput == "computer":
        global selcdirec
        selcdirec = selcdirec + "computer"
        print("directory: " + selcdirec)
        direcinput = input("Input Directory:")
#DIRECTORYDETECTORS
#LOADING CODE
print("P OS V0.1 LOADING")
while loadpercent1 < 100:

    time.sleep(random.randint(1,2))
    loadpercent1 = loadpercent1 + random.randint(1,10)
    if loadpercent1 > 100:
        loadpercent1 = 100
    print ("P OS IS: " + str(loadpercent1) + " PERCENT LOADED")
print("P OS HAS LOADED")
print("Press I ForDirectorySelector, Press R To Power Off P OS")
#KeyPressDetect

KEYINPUT = input("Select What You Want To Do")
if KEYINPUT == "i":
    INPUTDIREC()
elif KEYINPUT == "r":
    print("P OS SHUTTING DOWN")
    sys.exit()
else:
    print("Invalid Option")


#KeyPressDetect