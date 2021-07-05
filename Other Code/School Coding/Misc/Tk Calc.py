#Tkinktercalc v1.1, made by PhonieZGaminZ

import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

# mode select

messagebox.showinfo("Calculator","Calculator Time!.")
mode = str(input("1 = plus, 2 = minus, 3 = divide and 4 = multiply"))

# addition

if mode == '1':
    modename = 'Addition'
    messagebox.showinfo("Calculator","The Mode You Have selected Is " + str(modename))
    num1 = str(input("Enter Num1"))
    num2 = str(input("Enter Num2"))
    sum = float(num1) + float(num2)
    messagebox.showinfo("Calculator","The Answer Is " + str(sum))
    messagebox.showinfo("Calculator","Done!")

# subtraction

elif mode == '2':
    modename = 'Subtraction'
    messagebox.showinfo("Calculator","The Mode You Have selected Is " + str(modename))
    num1 = str(input("Enter Num1"))
    num2 = str(input("Enter Num2"))
    sum = float(num1) - float(num2)
    messagebox.showinfo("Calculator","The Answer Is " + str(sum))
    messagebox.showinfo("Calculator","Done!")

# division

elif mode == '3':
    modename = 'Division'
    messagebox.showinfo("Calculator","The Mode You Have selected Is " + str(modename))
    num1 = str(input("Enter Num1"))
    num2 = str(input("Enter Num2"))
    sum = float(num1) * float(num2)
    messagebox.showinfo("Calculator","The Answer Is " + str(sum))
    messagebox.showinfo("Calculator","Done!")

# multiplication

elif mode == '4':
    modename = 'Multiplication'
    messagebox.showinfo("Calculator","The Mode You Have selected Is " + str(modename))
    num1 = str(input("Enter Num1"))
    num2 = str(input("Enter Num2"))
    sum = float(num1) /  float(num2)
    messagebox.showinfo("Calculator","The Answer Is " + str(sum))
    messagebox.showinfo("Calculator","Done!")
elif mode == '5':
    messagebox.showinfo("Calculator","Placeholder")
else:
    messagebox.showerror("Calculator","Error 002, Invalid Mode, Please Restart The Calculator")



