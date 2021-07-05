#Read READ ME, DO NOT IGNORE OR DELETE, for copyright details

while 1 == 1:
 data = input("Would you like to view global or user data, 1 for global , 2 for user")
 if data == "2":
  user = input("Username:")
  data = open('User_Data.txt').read()
  count = data.count(user)
  print("Reading Data")
  with open('User_Data.txt') as f:
      for line in f:
          count += line.count(user)
  print(user)
  print("Has Used Mathotron")
  print (count)
  print("times")
 if data == "1":
   print("would you like to view how many times mathotron has been used to times, divide, add or subtract")
   type = input("1 for times,2 for divide,3 for add, 4 for subtract")
 if type == "1":
      data = open('User_Data.txt').read()
      count = data.count("times")
      print("Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("times")
      print("Mathotron has multiplied")
      print (count)
      print("times")

 if type == "2":
      data = open('User_Data.txt').read()
      count = data.count("divide")
      print("Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("divide")
      print("Mathotron has divided")
      print (count)
      print("times")

 if type == "3":
      data = open('User_Data.txt').read()
      count = data.count("plus")
      print("Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("plus")
      print("Mathotron has added")
      print (count)
      print("times")
 if type == "4":
      data = open('User_Data.txt').read()
      count = data.count("minus")
      print("Reading Data")
      with open('User_Data.txt') as f:
          for line in f:
              count += line.count("minus")
      print("Mathotron has subtracted")
      print (count)
      print("times")
