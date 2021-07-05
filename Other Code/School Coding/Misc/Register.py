#This program must not be be modified, forged or copied for commercial purposes.
#This program may be modified, forged or copied for educational or personal use.
#Registration Program
#Joshua Zack (Copyright 2020)
#Version 1.2.1
#Very noice code
#macOS exclusive gang here..
#On the road to 100 lines of code. 99/100! 05/02/2020

#Changelog

#1.0 - register.py created
#1.1 - added login or signup messagebox, added password match detection, added password storage
#1.2 - added full login system
#1.2.1 - added datetime functionality

#imports

import os
import tkinter
import random
import sys
import datetime

#datetime

x = datetime.datetime.now()
thedate=(x.strftime("%x"))

#tkinter

from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()

#login or signup

login = messagebox.askquestion('Login','Do you already have an account with us?')
if login == 'yes': #login
    messagebox.showinfo('Login','Please enter your username.')
    username_ask=input("Enter username.")
    c=open("username.txt","r")
    username_read = c.read()
    if username_read==username_ask:
        messagebox.showinfo('Login','Please enter your password for account: '+username_read)
    else:
        messagebox.showerror('Incorrect','Username was not found, please try again.')
        sys.exit()
    password_ask=input("Enter password.")
    b=open("userpassword.txt","r")
    password_read = b.read()
    if password_read==password_ask:
        messagebox.showinfo('Welcome','Login succesful.')
        messagebox.showinfo('Hello, '+username_read,'Welcome. You are logged in as: '+username_read)
    else:
        messagebox.showinfo('Incorrect','Password is incorrect, please try again.')
        sys.exit()

#user data input

if login == 'no':
    messagebox.showinfo("Register","Please register for a new account.")
    firstname=input("What is your first name?")
    surname=input("What is your surname?")
    email=input("Please enter your email address")
    phone=int(input("Please enter your UK phone number."))
    username=input("Please select a username.")
    password=input("Please enter a password")
    passwordconfirm=input("Please confirm your password")

#data storage

if login == 'no':
    f = open( 'userinfo.txt', 'a' )
    f.write('firstname ='+repr(firstname)+'\n' )
    f.write('username= ='+repr(username)+'\n' )
    f.write('email ='+repr(email)+'\n' )
    f.write('phone ='+repr(phone)+'\n' )
    f.write('passwordconfirm ='+repr(passwordconfirm)+'\n' )
    f.write('date_registered ='+repr(thedate)+'\n')
    f.close()

#login credintials storage

if login == 'no':
    a = open( 'userpassword.txt', 'w+' )
    a.write(password)
    a.close()
    x = open( 'username.txt', 'w+' )
    x.write(username)
    x.close()

#password match detection

if login == 'no':
    if password == passwordconfirm:
        messagebox.showinfo("Account","Account successfully registered!")
    else:
        messagebox.showerror("Error","Passwords do not match, please try again.")
