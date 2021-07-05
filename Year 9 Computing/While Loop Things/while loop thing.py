#random number game, also made this as instructions were vague, also provided code was already
#error free
import random
number = 0
randnumber = random.randint(1,5)
times = 0
while number != randnumber and times < 3:#starts the while loop
    print("")#these are here to space the text out
    print(str(randnumber)+" is the correct number, here for demonstration")#says correct number for
    if times > 0:#testing
        print("")
        print("incorrect number")
    times = times+1
    try:
        print("")
        number = int(input("The number is between 1 and 5, guess the number"))#takes input
    except:
        print("")
        print("invalid input")
        times = 100
if times >2 and number != randnumber:#determines if you lost or win
    print("")
    print("you lose, or inputted the wrong number")
else:
    print("")
    print("you win!")
    
