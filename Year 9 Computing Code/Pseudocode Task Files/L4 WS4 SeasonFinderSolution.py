#L4 WS4 SeasonFinder.py
#Season finder with 4 errors pointed out

#input the month of the year and the program
#will tell you which season it is in

###"moth" of the year - spelling error in comment,not a bug
###since it will not affect the running of the program

month = input("Enter the month of year: )
###bug1: Missing "

#variable.title() converts to title case with capital first letter
### bug2: incorrect variable name Month
month = Month.title()

###bug2: single = sign instead of ==
if month == "December" or month = "January" or month == "February": 
    print(month,"is in Winter")
elif month == "March" or month == "April" or month == "May":
    print(month,"is in Spring")
elif month == "June" or month == "July" or month == "August":
    print(month,"is in Summer")
elif month == "September" or month == "October" or month == "December":
###bug 3:should be September, October, November
    Print(month,"is in Autumn") ###bug4: Print is capitalised
else:
    print("Check spelling of month.")
    
input("Press ENTER to quit")
