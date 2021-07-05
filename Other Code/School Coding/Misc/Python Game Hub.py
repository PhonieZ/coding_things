#-------------------------------------------------------------------------------
# Name:        PythonGameHub
# Purpose:     Playing an assortment of games
#
# Author:      PhonieZGaminZ
#
# Created:     28/11/2019
# Copyright:   (c) PhonieZGaminZ 2019
# Licence:     PhonieZGaminZ, No Mods Allowed
#-------------------------------------------------------------------------------
import time
import os

def load():
    print("loading")
    time.sleep(0.75)
    print("loading.")
    time.sleep(0.75)
    print("loading..")
    time.sleep(0.75)
    print("loading...")
    time.sleep(0.75)
    print("loading")
    time.sleep(0.75)
    print("loading.")
    time.sleep(0.75)
    print("loading..")
    time.sleep(0.75)
    print("loaded")
pass
def menu():
    print("Welcome to the python game hub! Select a game")
    time.sleep(1)
    print ("1 = Snake")
    GameSelec = input("GameCode:")
    if GameSelec == "1":
        print("The Game You Have Chosen Is Snake, GameCode:1")
        load()
        os.system('Snake.py')





    elif GameSelec == "2":
         print("The Game You Have Chosen Is Minesweeper , GameCode:2")
         load()



    else:
        print("Invalid GameCode,rebooting")
        menu()

pass

menu()