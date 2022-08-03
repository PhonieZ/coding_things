from datetime import datetime
seasons = ["Winter", "Spring","Summer", "Autumn"]
month = datetime.now().month
if  month <= 2   or month == 12:         
  season = 0
elif month >= 3 and month <= 5:              
  season = 1
elif month >= 6 and month <= 8:         
  season = 2
else:
  season = 3
print("It is "+ seasons[season])
