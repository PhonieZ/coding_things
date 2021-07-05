import random

command = input("Input Random Number Range In Format: num1 num2 ").split()
try:
    print(str(random.randint(int(minmaxcommand[0]),int(minmaxcommand[1])))+" is your random number")
except:
    print("Invalid Input")