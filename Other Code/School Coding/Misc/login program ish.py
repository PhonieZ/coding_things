


print ("Welcome User, Please Pick One Of The 2 Options...")
import time
time.sleep (2)

for _ in range(2):
    print ("Please Wait")
    time.sleep(0.5)
    print ("Please Wait.")
    time.sleep(0.5)
    print ("Please Wait..")
    time.sleep(0.5)
    print ("Please Wait...")

reeee = input("Login:L SignUp:S")

for _ in range(2):
    print ("Processing Request")
    time.sleep(0.5)
    print ("Processing Request.")
    time.sleep(0.5)
    print ("Processing Request..")
    time.sleep(0.5)
    print ("Processing Request...")

time.sleep(2)

else:
    print ("Invalid Option, Please Restart Program")
    time.sleep(2)
for _ in range(3):
    print ("Shutting Down")
    time.sleep(0.5)
    print ("Shutting Down.")
    time.sleep(0.5)
    print ("Shutting Down..")
    time.sleep(0.5)
    print ("Shutting Down...")

if reeee == "L":
    print ("You Selected: Login")
    time.sleep(1)
    user = input("Username:")
    print("indexing...")
    open("userthing_storeuser", "r")
    user.index(user)
    print (user.read[user])


if reeee == "S":
    time.sleep(1)
    print ("You Selected: SignUp")
    time.sleep(2)
    print ("Please Insert Username...")
    textinput = input("Username:")
    print ("username:textinput")
    file = open('userthing_storeuser', 'w')
    file.write(textinput)
    file.close()

    print ("Please Insert Password...")
    textinput = input ("Password:")
    print ("password:textinput")
    file = open('userthing_storepass', 'w')
    file.write (textinput)
    file.close()
    print ("Finished!")
    print ("You have finished, please restart the program to continue...")
    time.sleep(2)

for _ in range(3):
        print ("Shutting Down")
        time.sleep(0.5)
        print ("Shutting Down.")
        time.sleep(0.5)
        print ("Shutting Down..")
        time.sleep(0.5)
        print ("Shutting Down...")






