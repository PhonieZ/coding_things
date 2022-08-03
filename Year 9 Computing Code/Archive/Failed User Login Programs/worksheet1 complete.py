firstname = ""
surname = ""
optione=""
username=""
def option():
    global optione
    global firstname
    global surname
    global username
    optione = input("Input your username if you are an existing user, if not then input x")
    if optione =="x":
        signup()
    else:
        login()
def login():
    global optione
    global firstname
    global surname
    global username
    if optione == username:
        print("You have successfully logged in "+username)
        option()
    else:
        print("Invalid option")
        option()

def signup():
    global optione
    global firstname
    global surname
    global username
    firstname = input("What is your firstname?")
    surname = input("What is your surname?")
    username = surname[0]+surname[1]+surname[2]+firstname[0]+str(len(surname))
    print("Your username is "+username)
    option()

option()


