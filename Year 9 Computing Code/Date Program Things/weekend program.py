import sys
print("What day is it today?")
try:
    day = int(input())
except:
    print("Invalid Input, Please Input Day In The 1-7 Numerical Format")
    sys.exit()
if day <= 4:
  remaining =6-day
  print("It’s A Weekday, "+str(remaining)+" Days Left!")
elif day == 5:
    print("Today Is Friday! 1 Day Left Until The Weekend!")
else:
  print("It’s The Weekend!")
