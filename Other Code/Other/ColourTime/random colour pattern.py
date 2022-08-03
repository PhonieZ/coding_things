#importing modules
from tkinter import Tk, Canvas, Frame, BOTH
import sys
import random
import time
#defining variables
col1 = "black"
wait = 1
#creating the window
root = Tk()
c = Canvas(root,height = 500,width=500)
c.pack()
#adding the colour grid
r1 = c.create_rectangle(20,20,100,100,fill=col1)
#displaying the window
c.pack()
root.mainloop
time.sleep(1)
#changing the colour of the colour grid
#while True:
time.sleep(wait)
num =random.randint(1,4)
if num == 1:
    col1="black"
elif num == 2:
    col1="white"
elif num == 3:
    col1="light grey"
else:
    col1="grey"
print(col1)
c.itemconfig(r1,fill=col1)
    

    
    
