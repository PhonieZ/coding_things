#v0.5
username=""
password=""
option=""
id=""
import  time
import random

def selc():
    global username
    global password
    global option
    print(option)
    option = input("2 for signin, 1 for login")
    print(option)
    if option == "2":
        print("e")
        signup()
    elif option == "1":
        print("z")
        login()
    else:
        print("Invalid Option")

def optione():
    print("3")
    global username
    global option
    global password
    print(option)
    selc()

def login():
    print("1")
    global username
    global password
    username = input("Username:")
    password = input("Password:")
    print("done")
    time.sleep(2)
    option()

def signup():
    print("2")
    data = open('User_Data_Things.txt').read()
    count = data.count(str(id))
    global username
    global password
    global id
    username = input("Username:")
    if len(username) > 30:
        print("Username too long, please retry")
        time.sleep(1)
        selc()
    else:
        print("")
    password = input("Password:")
    id = str(random.randint(1,9000))
    f = open('User_Data_Things.txt','a')
    f.write("\n" + "")
    f.write("\n" + username)
    f.write("\n" + password)
    f.write("\n" + id)
    f.close()
    print("good job "+username+" you log in, also your id is "+id+" don't forget that.")
    time.sleep(2)
    optione()

optione()




