import random as poo
with open('funny.txt', "r") as funny:
    heehee = funny.read().split(' ')
heeheeamount=len(heehee)-1
print(heeheeamount)
while True:
  print(heehee[poo.randint(0,heeheeamount)])