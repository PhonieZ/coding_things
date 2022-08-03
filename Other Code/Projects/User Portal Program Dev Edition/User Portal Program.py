# This is the rewrite of J.Zaceks user program, now renamed to user portal program
# Copyright: do not edit or redistribute without PhonieZgaminZ's permission
# This is v0.3
# Error Notes
# Error 001 = ivalid option
# Error 002 = Invalid Password Confirmation
#
#
#
#
#
#
#
# Update Log:
#
#
#
#
#
#
#
#
#
#
#
#
# End Of Update log:

# Imports

import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()
import random
# Imports

# Main Program

# Selection Menu

messagebox.showinfo("User Portal Program","Welcome To The User Portal, Select An Option Shortly")
option = str(input("1 = login, 2 = sign up"))

# login, signup detector

if option == '1':
    print("1")



elif option == '2':
    print("2")
    # gets details
    FirstName = str(input("Enter Your First Name"))
    LastName = str(input("Enter Your Last Name"))
    UserName = str(input("Enter Your Username"))
    Email = str(input("Enter Your Email"))
    Password = str(input("Enter Your Password"))
    PasswordConfirm = str(input("Confirm Your Password"))
    # checks if password confirm was correct
    if Password == PasswordConfirm:
         print("2-1")
         messagebox.showinfo("User Portal Program","Account Created Succesfully!")
         f = open('User_Data.txt','a')
         f.write('\n' + '')
         f.write('\n' + '')
         f.write('\n' + '')
         f.write('\n' + 'First Name:')
         f.write('\n' + FirstName )
         f.write('\n' + 'Last Name:')
         f.write('\n' +  LastName )
         f.write('\n' + 'User Name:')
         f.write('\n' +  UserName )
         f.write('\n' + 'Email:')
         f.write('\n' +  Email )
         f.write('\n' +  'Password:' )
         f.write('\n' +  Password )
         print("2-2")
    else:
         print("2-2")
         messagebox.showerror("User Portal Program","Error 002,Invalid Password Confirmation, Please Restart Program")
         print("2-2check")



else:
    messagebox.showerror("User Portal Program","Error 001,Invalid Option , Please Restart Program")
    print("null")



