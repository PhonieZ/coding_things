#importing and defining variables
import random
from statistics import mode
i = 0
run = 1
chance = 0
set = ""
#defining funtions
def datacreate():
    tims = open("times.txt,"r")
    lineread = tims.readlines
    lineread[0]
    tims.close()
    linecreate = open("times.txt","w")
    linecreate.writelines(lineread)
    linecreate.close()
def lineread():
    
def dataproccess():
    while i < 20:
        i = i + 1
        chance = random.randint(1,3)
        set = set + str(chance)+","
        if i == 20:
            set = set + str(chance)
            set = set.split(",")
            set = mode(set)
    print(set)
def linereq():
    dataread = open("DataRun"+run+".txt", "r")
    linerequest = dataread.readlines()
    linerequest[1] = "text"+"\n"
    dataread.close()
def linewrite():
    datawrite = open("DataRun"+run+".txt", "w")
    datawrite.writelines(linerequest)
    datawrite.close()
if os.path.isfile("times.txt"):
    lineread()
else:
    datacreate()

