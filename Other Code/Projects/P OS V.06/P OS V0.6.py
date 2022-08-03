#P OS V0.6,DO NOT USE CODE COMMERCIALLY OR USE THIS CODE WITHOUT CREDIT TO ORIGINAL OWNER OF P OS, P OS IS ALL ASSETS OF PHONEZ 2020 AND BEYOND
#IMPORTS
import time
import random
import re
import sys
#VARIABLES
version = "0.6"
firstname = ""
surname = ""
optione=""
user_data = []
username=""
password = ""
passcheck = 0
crypt = ""
equation =""
magic = ""
dice = 0
loadpercent1 = 0
selcdirec = ""
#LOGINSHIT
def option():
    global passcheck
    global optione
    global loadpercent1
    loadpercent1 = 0
    print("P OS " + version +" LOADING")
    while loadpercent1 < 100:

        time.sleep(0.5)
        loadpercent1 = loadpercent1 + random.randint(10,15)
        if loadpercent1 > 100:
            loadpercent1 = 100
        print ("P OS IS: " + str(loadpercent1) + " PERCENT LOADED")
    print("P OS HAS LOADED")
    optione = input("INPUT USERNAME FOR LOGIN, INPUT X FOR SIGNUP:")
    if optione =="x":
        signup()
    else:
        login()
def login():
    global user_data
    global passcheck
    global password
    global optione
    global username
    with open('User_Stuff.txt','r') as p:
        lines = p.read().split("\n")
    for i,line in enumerate(lines):
        global user_data
        if optione in line.split():
            global user_data
            with open("User_Stuff.txt","r") as x:
                y = x.readlines()
                dd = y[i]
                user_data = dd.split()
    if optione == user_data[0]:
        optione = input("ENTER PASSWORD "+username+":")
        if optione == user_data[1]:
            print(username+" SUCCESFULLY LOGGED IN")
            time.sleep(1)
            LOAD()
        else:
            print("INVALID PASSWORD "+username)
            option()
    else:
        print("INVALID USERNAME")
        option()
def signup():
    global user_data
    global password
    global optione
    global firstname
    global surname
    global username
    firstname = input("FIRSTNAME:")
    surname = input("SURNAME:")
    password = input("PASSWORD:")
    username = surname[0] + surname[1] + surname[2] + firstname[0] + str(len(surname))
    username = username.lower()
    with open("User_Stuff.txt", "a+") as f:
        f.write("\n" + "   ")
        f.write("\n" + username + " " + password)
    print("USERNAME: "+username+" PASSWORD: "+password)
    option()
#APPFUNCTIONS
def CRYPTICRUN():
    global loadpercent1
    loadpercent1 = 0
    while loadpercent1 < 100:
        time.sleep(0.125)
        loadpercent1 = loadpercent1 + random.randint(10,20)
        if loadpercent1 > 100:
            loadpercent1 = 100
        print ("Cryptic Is: " + str(loadpercent1) + " Percent Loaded")
    print("Cryptic Loaded")
    global crypt
    def keyr():
        print("Cryptic Shutting Down")
        time.sleep(1)
        MENULOAD()
    while True:
        crypt = input("Input Valid Equation, Input r To Quit")
        if crypt == "r":
            keyr()
        else:
            keyq()
def CALC():
    global loadpercent1
    loadpercent1 = 0
    while loadpercent1 < 100:
        time.sleep(0.125)
        loadpercent1 = loadpercent1 + random.randint(10,20)
        if loadpercent1 > 100:
            loadpercent1 = 100
        print ("Calculator Is: " + str(loadpercent1) + " Percent Loaded")
    print("Calculator Loaded")
    global equation
    def keyq():
        global equation
        print ("The Anwser Is:")
        print (eval(equation))
        equation = ""
    def keyr():
        print("Calculator Shutting Down")
        time.sleep(1)
        MENULOAD()
    while True:
        equation = input("Input Valid Equation, Input r To Quit")
        if equation == "r":
            keyr()
        else:
            keyq()
def MAGIC8BALL():
    global username
    global loadpercent1
    loadpercent1 = 0
    while loadpercent1 < 100:
        time.sleep(0.125)
        loadpercent1 = loadpercent1 + random.randint(10,20)
        if loadpercent1 > 100:
            loadpercent1 = 100
        print ("Magic8Ball Is: " + str(loadpercent1) + " Percent Loaded")
    print("Magic8Ball Loaded")
    global magic
    global dice
    def magics():
        global magic
        global dice
        print("Hello "+magic+" Ask Me a Question")
        input("Go On, Ask Me Something!: ")
        print("I am thinking!")
        dice = random.randint(1,9)
        time.sleep(random.randint(1,3))
        if dice == 1:
                   print("No I Don't Think So...")
                   time.sleep(1)
                   magici()
        elif dice == 2:
                   print("What?")
                   time.sleep(1)
                   magici()
        elif dice == 3:
                   print("Yeah Bro!")
                   time.sleep(1)
                   magici()
        elif dice == 4: 
                   print("Thats A Sick Question, Course!")
                   time.sleep(1)
                   print("*coughs* Great Now I Am Sick, Well I Am G *coughs again* Okay Maybe No *coughs violently* Oh Fu *collapses* ")
                   time.sleep(4)
                   magici()
        elif dice == 5:
                   print("Oh No No No No No No No No No, Never Ever, NOOOOOOOOOOOOOOOOOOOOOOOOOO, Just No")
                   time.sleep(1)
                   magici()
        elif dice == 6:
                   print("Oh Yes  Yes Yes  Yes Yes  Yes Yes  Yes , Yeeeeeeeeeeeeee, Thats All I Have To Say...")
                   time.sleep(1)
                   print("Okay Maybe Not, YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEES, Ok I Think Thats All...")
                   time.sleep(1)
                   print("YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEES")
                   time.sleep(1)
                   magici()
        elif dice == 7:
                   print("nO")
                   time.sleep(1)
                   magici()
        elif dice == 8:
                   print("yEs")
                   time.sleep(1)
                   magici()
        elif dice == 9:
                   print("What Did You Say Again?")
                   time.sleep(1)
                   magici()
    def magicr():
        print("Magic8Ball Shutting Down")
        time.sleep(1)
        MENULOAD()
    def magici():
        global username
        global magic
        while True:
            magic = username
            magice = input("Hello"+username+" Remember To Input r To Quit: ")
            if magice == "r":
                magicr()
            else:
                magics()
    magici() 

#APPFUNCTIONS
#DIRECTORYINPUTS
def LOAD():
    global loadpercent1
    loadpercent1 = 0
    print("P OS " + version +" MENU LOADING")
    while loadpercent1 < 100:

        time.sleep(0.5)
        loadpercent1 = loadpercent1 + random.randint(15,20)
        if loadpercent1 > 100:
            loadpercent1 = 100
        print ("P OS MENU IS: " + str(loadpercent1) + " PERCENT LOADED")
    print("P OS Has Loaded")
    MENU()
def INVALID():
    print("Invalid Option")
def INVALIDKEY():
    print("Invalid Key")
def MENULOAD():
    global loadpercent1
    loadpercent1 = 0
    while loadpercent1 < 100:
        time.sleep(0.25)
        loadpercent1 = loadpercent1 + random.randint(10,20)
        if loadpercent1 > 100:
            loadpercent1 = 100
        print ("Menu Is: " + str(loadpercent1) + " Percent Loaded")
    print("Menu Loaded")
    MENU()

def INVALIDMENU():
    print("Invalid Option")
    time.sleep(3)
    MENULOAD()
def COMPUTER():
    global selcdirec
    selcdirec = selcdirec + "computer"
    print("directory: " + selcdirec)
    direcinput = input("Input Directory: ")
    if direcinput == "applications":
        APPLICATIONS()
    else:
        INVALIDMENU()
def APPLICATIONS():
    global selcdirec
    selcdirec = selcdirec + "/applications"
    print("directory: " + selcdirec)
    direcinput = input("Input Directory: ")
    if direcinput == "calculator":
        CALCULATOR()
    elif direcinput == "magic8ball":
        MAGIC8BALLRUN()
    else:
        INVALIDMENU()
def CRYPTIC():
    global selcdirec
    selcdirec = selcdirec + "/cryptic"
    print("directory: " + selcdirec)
    direcinput = input("Do You Want To Run " + selcdirec + " Y or N: ")
    if direcinput == "y":
        CRYPTICRUN()
    elif direcinput == "n":
        print("Booting Back To Menu")
        time.sleep(1)
        MENULOAD()
def CALCULATOR():
    global selcdirec
    selcdirec = selcdirec + "/calculator"
    print("directory: " + selcdirec)
    direcinput = input("Do You Want To Run " + selcdirec + " Y or N: ")
    if direcinput == "y":
        CALC()
    elif direcinput == "n":
        print("Booting Back To Menu")
        time.sleep(1)
        MENULOAD()
def MAGIC8BALLRUN():
    global selcdirec
    selcdirec = selcdirec + "/magic8ball"
    print("directory: " + selcdirec)
    direcinput = input("Do You Want To Run " + selcdirec + " Y or N: ")
    if direcinput == "y":
        MAGIC8BALL()
    elif direcinput == "n":
        print("Booting Back To Menu")
        time.sleep(1)
        MENULOAD()
def PHELP():
    global version
    global pgselc
    print("P Help V "+version+" Selected")
    print("Note: It Is Recommended To Vist Page 1 Of P Help V "+version+" To Learn Where To Find Specific Help Pages")
    pgselc = input("Input The Page Do You Want To Select, Input R To Quit P Help V "+ version+": ")
    if pgselc == "1":
        print("This help page documents all the help pages and what they contain,")
        print("page 2 tells you basic functions in the menu")
        print("page 3 tells you how to launch an application")
        print("page 4 tells you all the currently installed applications")
        print("These are all the help pages that that have been created.")
        print("P Help V "+version)
        time.sleep(3)
        MENU()
    elif pgselc == "2":
        print("If you would want to input and directory,")
        print("first go to the menu,")
        print("then input i when it prompts you to,")
        print("to learn more about the directory input, and how to use it, visit page 3 on P Help "+ version+" or what you are on right now.")
        print("If you would want to power off P OS "+version)
        print("first go to the menu,")
        print("then input r when it prompts you to.")
        print("P Help V "+version)
        time.sleep(3)
        MENU()
    elif pgselc == "3":
        print("If you want to run  an application for example, the calculator, you would first input computer, this would mean you are brwosing the computer directory,")
        print("then you would input applications to open up the applications directory,")
        print("and finally to open the calculator you would input calculator, then when it prompts you if you want to launch calculator, input y and it will open.")
        print("If you would want to quit the calculator, input r instead of an equation , and you will be booted back to the menu.")
        print("P Help V "+version)
        time.sleep(3)
        MENU()
    elif pgselc == "4":
        print("Currently Installed Applications Are,")
        print("calculator and magic8ball,")
        print("remember to browse in the applications directory for these applications")
        print("P Help V "+version)
        time.sleep(3)
        MENU()
    elif pgselc == "r":
        print("P Help V "+version+" Shutting Down")
        time.sleep(1)
        MENULOAD()
    else:
        INVALIDMENU()
def MENU():
    print("Press H For Help")
    KEYINPUT = input("Input What You Want To Do: ")
    if KEYINPUT == "i":
        INPUTDIREC()
    elif KEYINPUT == "r":
        print("Thank You For Using P OS V "+version+" P OS Is Now Shutting Down")
        time.sleep(random.randint(1,3))
        sys.exit()
    elif KEYINPUT == "h":
        PHELP()
    else:
        INVALIDMENU()
#DIRECTORYDETECTORS
def INPUTDIREC():
    global selcdirec
    print("DirecInput V "+version+" Selected")
    selcdirec = ""
    direcinput = input("Input Directory: ")
    if direcinput == "computer":
        COMPUTER()
    else:
        INVALIDMENU()
#LOADING CODE
option()
