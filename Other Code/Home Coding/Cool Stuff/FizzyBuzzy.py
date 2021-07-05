import sys
num1 = 5
num2 = 3
nump = 0
num = 0
output = ""
togoto = input("Input Times:")
try:
    int(togoto)*1
except:
    print("Invalid Input")
    sys.exit()
while int(nump)<int(togoto):
    output = ""
    num = 0
    nump = nump + 1
    if nump % num1 == 0:
        output = output + "fizz"
        num = 1
    if  nump % num2 == 0:
        output = output + "buzz"
        num = 1
    elif  nump % num2 == 0:
        output = output + "buzz"
        num = 1
    elif num == 1:
        output=output
    else:
        output = output + str(nump)
    print(output)


