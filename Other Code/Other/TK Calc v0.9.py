from tkinter import *
from tkinter import messagebox
import sys
import tkinter as tk
root = tk.Tk()
root.withdraw()
import random
equation = ""

def key1():
    global equation
    equation = equation + "1"
    print (equation)
    text = tk.Label(root,text="" + equation)
    text.mainloop
def key2():
    global equation
    equation = equation + "2"
    print (equation)
    text = tk.Label(root,text="" + equation)
def key3():
    global equation
    equation = equation + "3"
    print (equation)
    text = tk.Label(root,text="" + equation)

def key4():
    global equation
    equation = equation + "4"
    print (equation)
    text = tk.Label(root,text="" + equation)

def key5():
    global equation
    equation = equation + "5"
    print (equation)
    text = tk.Label(root,text="" + equation)

def key6():
    global equation
    equation = equation + "6"
    print (equation)
    text = tk.Label(root,text="" + equation)

def key7():
    global equation
    equation = equation + "7"
    print (equation)
    text = tk.Label(root,text="" + equation)

def key8():
    global equation
    equation = equation + "8"
    print (equation)
    text = tk.Label(root,text="" + equation)
def key9():
    global equation
    equation = equation + "9"
    print (equation)
    text = tk.Label(root,text="" + equation)
def key0():
    global equation
    equation = equation + "0"
    print (equation)
    text = tk.Label(root,text="" + equation)
def keyplus():
    global equation
    equation = equation + "+"
    print (equation)
    text = tk.Label(root,text="" + equation)
def keyminus():
    global equation
    equation = equation + "-"
    print (equation)
    text = tk.Label(root,text="" + equation)
def keytimes():
    global equation
    equation = equation + "*"
    print (equation)
    text = tk.Label(root,text="" + equation)
def keydivide():
    global equation
    equation = equation + "/"
    print (equation)
    text = tk.Label(root,text="" + equation)
def keye():
    global equation
    print ("Reset Input")
    equation = ""
    text = tk.Label(root,text="" + equation)
def keyq():
    global equation
    print ("The Answer Is:")
    print (eval(equation))
    text = tk.Label(root,text="" + equation)
    text.pack()
    equation = ""
   
def keyr():
    sys.exit()
top = Tk()
top.geometry("250x200")
text = tk.Label(root,text="" + equation)

text.place(x = 0,y =35)
B = Button(top, text = "1", command = key1)
B.place(x = 0,y = 55)
B = Button(top, text = "2", command = key2)
B.place(x = 25,y = 55)
B = Button(top, text = "3", command = key3)
B.place(x = 45,y = 55)
B = Button(top, text = "4", command = key4)
B.place(x = 65,y = 55)
B = Button(top, text = "5", command = key5)
B.place(x = 85,y = 55)
B = Button(top, text = "6", command = key6)
B.place(x = 105,y = 55)
B = Button(top, text = "7", command = key7)
B.place(x = 0,y = 75)
B = Button(top, text = "8", command = key8)
B.place(x = 25,y = 75)
B = Button(top, text = "9", command = key9)
B.place(x = 45,y = 75)
B = Button(top, text = "0", command = key0)
B.place(x = 65,y = 75)
B = Button(top, text = "+", command = keyplus)
B.place(x = 105,y = 75)
B = Button(top, text = "-", command = keyminus)
B.place(x = 125,y = 75)
B = Button(top, text = "*", command = keytimes)
B.place(x = 145,y = 75)
B = Button(top, text = "/", command = keydivide)
B.place(x = 165,y = 75)
B = Button(top, text = "AC", command = keye)
B.place(x = 105,y = 105)
B = Button(top, text = "=", command = keyq)
B.place(x = 135,y = 105)
B = Button(top, text = "Quit", command = keyr)
B.place(x = 45,y = 105)

equation = ""
root.mainloop
def keypress(event):

    if event.keysym == 'Escape':
        root.destroy()

    x = event.char
    if x == "1":
        key1()
    elif x == "2":
        key2()
    elif x == "3":
        key3()
    elif x == "4":
        key4()
    elif x == "5":
        key5()
    elif x == "6":
        key6()
    elif x == "7":
        key7()
    elif x == "8":
        key8()
    elif x == "9":
        key9()
    elif x == "0":
        key0()
 
    elif x == "+":
        keyplus()
    elif x == "/":
        keydivide()
    elif x == "*":
        keytimes()
    elif x == "-":
        keyminus()
    elif x == "q":
        keyq()
    elif x == "e":
        keye()
    elif x == "r":
        sys.exit()
    else:
        1==1



root = tk.Tk()
#print ("Press a key (Escape key to exit):")
root.bind_all('<Key>', keypress)
root.withdraw()
root.mainloop()





