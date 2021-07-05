#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m.aydin
#
# Created:     28/11/2018
# Copyright:   (c) m.aydin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

dumbarray = []


reee = input("Hello, Welcome To This Boring-ish datbase of names! Login or Signup? [L or S]")

if reee == "L":
    print("Username:")
    gayusernamesrc = input("")
    print("indexing...")
    with open("userthing_storeuser", "r") as foo:
        dumbarray = foo.readlines(all)
    x = gayusernamesrc.index(gayusernamesrc)
    print (dumbarray[x])


if reee == "S":
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
    file.write( textinput)
    file.close()
    print ("Finished!")




