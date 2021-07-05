#Read READ ME, DO NOT IGNORE OR DELETE, for copyright details
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

import time
while 1 == 1:
 data = input("Would you like to view global or user data, 1 for global , 2 for user")
 if data == "2":
  user = input("Username:")
  data = open('User_Data.txt').read()
  count = data.count(user)
  messagebox.showinfo("Mathotron Statistic Viewer","Reading Data")
  with open('User_Data.txt') as f:
      for line in f:
          count += line.count(user)
  messagebox.showinfo("Mathotron Statistic Viewer",str(user) + " Has Used Mathotron " + str(count) + " Times")
 if data == "1":
   messagebox.showinfo("Mathotron Statistic Viewer","would you like to view how many times mathotron has been used to times, divide, add or subtract")
   type = input("1 for times,2 for divide,3 for add, 4 for subtract")
 if type == "1":
      data = open('User_Data.txt').read()
      count = data.count("times")
      messagebox.showinfo("Mathotron Statistic Viewer","Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("times")
      messagebox.showinfo("Mathotron Statistic Viewer","Mathotron Has Multiplied " + str(count) + " Times")

 if type == "2":
      data = open('User_Data.txt').read()
      count = data.count("divide")
      messagebox.showinfo("Mathotron Statistic Viewer","Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("divide")
      messagebox.showinfo("Mathotron Statistic Viewer","Mathotron Has Divided " + str(count) + " Times")

 if type == "3":
      data = open('User_Data.txt').read()
      count = data.count("plus")
      messagebox.showinfo("Mathotron Statistic Viewer","Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("plus")
      messagebox.showinfo("Mathotron Statistic Viewer","Mathotron Has Added " + str(count) + " Times")
 if type == "4":
      data = open('User_Data.txt').read()
      count = data.count("minus")
      messagebox.showinfo("Mathotron Statistic Viewer","Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("minus")
      messagebox.showinfo("Mathotron Statistic Viewer","Mathotron Has Subtracted " + str(count) + " Times")
