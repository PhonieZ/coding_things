#Read READ ME, DO NOT IGNORE OR DELETE, for copyright details
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

import time
while 1 == 1:
    username = input("Username:")
    messagebox.showinfo("Mathotron","Hello " + str(username))

    f = open('User_Data.txt','a')
    f.write('\n' + '')
    f.write('\n' + '')
    f.write('\n' + '')
    f.write('\n' + 'user:')
    f.write('\n' + username )
    f.close()
    mode = input("select a mode, plus , minus , times or divide")
    if mode == "plus":
        messagebox.showinfo("Mathotron","Addition Mode Selected")
        Num1 = input("Num1:")
        messagebox.showinfo("Mathotron","Number 1 Is: "+ str(Num1))
        Num2 = input("Num2:")
        messagebox.showinfo("Mathotron","Number 2 Is: "+ str(Num2))
        ans = int(Num1) + int(Num2)
        messagebox.showinfo("Mathotron","The Equation Is "+ str(Num1 ) +" + "+ str(Num2))
        messagebox.showinfo("Mathotron","The Answer Is: "+ str(ans))
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    elif mode == "minus":
        messagebox.showinfo("Mathotron","Subtraction Mode Selected")
        Num1 = input("Num1:")
        messagebox.showinfo("Mathotron","Number 1 Is: "+ str(Num1))
        Num2 = input("Num2:")
        messagebox.showinfo("Mathotron","Number 2 Is: "+ str(Num2))
        ans = int(Num1) - int(Num2)
        messagebox.showinfo("Mathotron","The Equation Is "+ str(Num1 ) +" - "+ str(Num2))
        messagebox.showinfo("Mathotron","The Answer Is: "+ str(ans))
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    elif mode == "times":
        messagebox.showinfo("Mathotron","Multiplication Mode Selected")
        Num1 = input("Num1:")
        messagebox.showinfo("Mathotron","Number 1 Is: "+ str(Num1))
        Num2 = input("Num2:")
        messagebox.showinfo("Mathotron","Number 2 Is: "+ str(Num2))
        ans = int(Num1) * int(Num2)
        messagebox.showinfo("Mathotron","The Equation Is "+ str(Num1 ) +" x "+ str(Num2))
        messagebox.showinfo("Mathotron","The Answer Is: "+ str(ans))
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    elif mode == "divide":
        messagebox.showinfo("Mathotron","Division Mode Selected")
        Num1 = input("Num1:")
        messagebox.showinfo("Mathotron","Number 1 Is: "+ str(Num1))
        Num2 = input("Num2:")
        messagebox.showinfo("Mathotron","Number 2 Is: "+ str(Num2))
        ans = int(Num1) / int(Num2)
        messagebox.showinfo("Mathotron","The Equation Is "+ str(Num1 ) +" / "+ str(Num2))
        messagebox.showinfo("Mathotron","The Answer Is: "+ str(ans))
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    else:
        messagebox.showinfo("Mathotron","Invalid Option, Please Reboot Mathotron...")
        time.sleep(3)








