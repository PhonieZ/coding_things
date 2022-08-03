from datetime import datetime
day = datetime.now().weekday()
if day <= 3:
  remaining =5-day
  print("It’s A Weekday, "+str(remaining)+" Days Left!")
elif day == 4:
    print("Today Is Friday! 1 Day Left Until The Weekend!")
else:
  print("It’s The Weekend!")
