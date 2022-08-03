import sys#for exiting program in code
count=0#initialises count var
running_total=0#initialises running total var
number=input("input first number,0 to exit")#gets first input
try:#this just checks if it is an int
    number=int(number)#converts string to int
except:#if it is not int is does what is inside
    sys.exit("invalid input(input not integer) restart to continue")#exits program with detailed notes
while number != 0:#starts while loop
    count+=1#adds to count
    running_total=running_total+number#adds to running total
    number=input("input next number,0 to exit")#gets new input
    try:#this just checks if it is an int
        number=int(number)#converts string to int
    except:#if it is not int is does what is inside
        sys.exit("invalid input(input not integer) restart to continue")#exits program with detailed notes
sys.exit("number count: "+str(count)+" total: "+str(running_total))#gives output and exits for user
