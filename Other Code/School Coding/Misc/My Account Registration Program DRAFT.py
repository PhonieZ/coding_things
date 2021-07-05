
# credit to M.aydin
# and J.Zacek
# noice
# this is v1.3 of version


# imports

import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()
import random

# message things

messagebox.showwarning("Register For Account","To continue using our services, please create an account.")
firstname = str(input("Please enter your first name."))
surname = input("Please enter your surname")
email = input("Please enter you email address.")
username = input("Please choose a username for your account.")
password = str(input("Please make a password for your account"))
passwordconfirm = str(input("Please confirm your password."))

# password checker
def passconfirm():
    if password == passwordconfirm:
        messagebox.showinfo("Thank you",'Thank you for registering ' + str(username))
        messagebox.showerror("Credit Score","Your credit score is "+ str(random.randint(300,579))
    else:
        messagebox.showinfo("Thank you",'Thank you for registering ' + str(username))
        passconfirm()


