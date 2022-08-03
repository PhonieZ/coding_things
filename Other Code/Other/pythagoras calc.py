import math
nums=""
numlist=['']
num1=0
num2=0
def inpute():
    global nums
    global numlist
    numlist=input("2 side vals to give hypotenuse").split()
    check()
def check():
    global nums
    global numlist
    global num1
    global num2
    if len(numlist) < 2 or len(numlist) > 2:
        print("invalid")
        inpute()
    try:
        num1=float(numlist[0])
        num2=float(numlist[1])
    except:
        print("invalid")
        inpute()
    calc()
def calc():
    output=math.sqrt(num1*num1+num2*num2)
    print(str(output)+" is hypotenuse")
    inpute()
inpute()
