import random
roll_total=1
roll=random.randint(1,6)
while roll != 6:
    print("You rolled a "+str(roll))
    roll_total = roll_total+1
    roll = random.randint(1,6)
if roll_total==1:
    print("It took you "+str(roll_total)+" roll until you rolled a 6")
else:
    print("It took you "+str(roll_total)+" rolls until you rolled a 6")
