import random
import sys
import time
delay = 1.1
commands = ["quit","randint","randfloat","commandexample","error0","error1","cmdinput","help","fizzbuzz","logout","userhub"]
logged = 0
optione=""
user_data = []
username=""
password = ""
passcheck = 0
def option():
    global passcheck
    global optione
    optione = input("Input A Username")
    login()
def login():
    global user_data
    global passcheck
    global password
    global optione
    global username
    global logged
    with open('User_Stuff.txt','r') as p:
        lines = p.read().split("\n")
    for i,line in enumerate(lines):
        global user_data
        if optione in line.split():
            global user_data
            with open("User_Stuff.txt","r") as x:
                yy = x.readlines()
                dd = yy[i]
                user_data = dd.split()
    try:
        if optione == user_data[0]:
            username = user_data[0]
            optione = input("Please Enter Your Password "+username+": ")
            if optione == user_data[1]:
                print("You have logged in succesfully "+username+"!")
                time.sleep(1)
                logged = 1
                cmdinput()
            else:
                print("Invalid Password "+username)
                option()
    except:
        if logged == 1:
            sys.exit()
        else:
            print("Existing Username Not Detected, Booting To Signup...")
            time.sleep(1)
            signup()

def signup():
    global user_data
    global password
    global optione
    global firstname
    global surname
    global username
    username = optione
    password = input("What is your password?")
    with open("User_Stuff.txt", "a") as f:
        f.write("\n" + username + " " + password)
    print("Your username is "+username+" and your password is "+password)
    username = ""
    option()
def cmdprocess():
    global command
    global commands
    if command[0] == commands[0]:
        quit()
    elif command[0] == commands[1]:
        randint()
    elif command[0] == commands[2]:
        randfloat()
    elif command[0] == commands[3]:
        commandexample()
    elif command[0] == commands[4]:
        invalidsyntax0()
    elif command[0] == commands[5]:
        invalidsyntax1()
    elif command[0] == commands[6]:
        cmdinput()
    elif command[0] == commands[7]:
        help()
    elif command[0] == commands[8]:
        fizzbuzz()
    elif command[0] == commands[9]:
        logout()
    elif command[0] == commands[10]:
        userhub()
    else:
        invalidsyntax1()
def cmdinput():
    global command
    global commands
    global delay
    time.sleep(1)
    command = input("Input Command").split()
    cmdprocess()

def commandexample():
    global command
    global commands
    print("This Is An Example Command")
    cmdinput()

def userhub():
    global command
    global commands
    print("nothing here "+username+" lol")
    cmdinput()

def logout():
    global command
    global commands
    print("Logging Out")
    time.sleep(1)
    option()

def fizzbuzz():
    global command
    global commands
    num1 = 5
    num2 = 3
    nump = 0
    num = 0
    output = ""
    togoto = command[1]
    try:
        int(togoto)*1
    except:
        print("Invalid Number")
        cmdinput()
    while int(nump)<int(togoto):
        output = ""
        num = 0
        nump = nump + 1
        if nump % num1 == 0:
            output = output + "fizz"
            num = 1
        if  nump % num2 == 0:
            output = output + "buzz"
            num = 1
        elif  nump % num2 == 0:
            output = output + "buzz"
            num = 1
        elif num == 1:
            output=output
        else:
            output = output + str(nump)
        print(output)
    cmdinput()

def help():
    global command
    global commands
    print("All the commands are: "+str(commands))
    cmdinput()

def delay():
    global command
    global commands
    global delay
    try:
        delay = float(command[1])
        print("Delay Is Now "+str(delay))
        cmdinput()
    except:
        invalidsyntax0()

def randint():
    global command
    global commands
    try:
        print(str(random.randint(int(command[1]),int(command[2])))+" Is Your Random Integer")
        cmdinput()
    except:
        invalidsyntax0()

def randfloat():
    global command
    global commands
    try:
        print(str(random.uniform(float(command[1]),float(command[2])))+" Is Your Random Float")
        cmdinput()
    except:
        invalidsyntax0()

def invalidsyntax0():
    print("Invalid Syntax (Error 0)")
    time.sleep(1)
    cmdinput()
def invalidsyntax1():
    print("Invalid Command (Error 1)")
    time.sleep(1)
    cmdinput()

def quit():
    global command
    global commands
    print("Shutting Down")
    sys.exit()
option()
