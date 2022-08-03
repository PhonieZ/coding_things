import time
import sys
firstname = ""
surname = ""
optione=""
user_data = []
username=""
password = ""
passcheck = 0
def option():
    global passcheck
    global optione
    optione = input("Input A Username Or r To Shut Down: ")
    #print(optione)
    if optione == "r":
        print("Shutting Down...")
        sys.exit()
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
                yy = x.readlines()
                dd = yy[i]
                user_data = dd.split()
                #print(user_data[0])
                #print(user_data[1])
    try:
        if optione == user_data[0]:
            username = user_data[0]
            optione = input("Please Enter Your Password "+username+": ")
            if optione == user_data[1]:
                print("You have logged in succesfully "+username+"!")
                time.sleep(1)
                option()
            else:
                print("Invalid Password "+username)
                option()
    except:
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
    password = input("What is your password? ")
    username = username.lower()
    with open("User_Stuff.txt", "a") as f:
        f.write("\n" + username + " " + password)
    print("Your username is "+username+" and your password is "+password)
    username = ""
    option()
option()


