firstname = input("What is your firstname?")
surname = input("What is your surname?")
capfirst = firstname.upper()
capsec = surname.upper()
firstcount = len(firstname)
surcount = len(surname)
fullcount = len(firstname+" "+surname)
initials = capfirst[0]+"."+capsec[0]
print("Hello "+firstname+" "+surname+" also your intials are "+initials)
print("Your firstname is "+str(firstcount)+" characters long, your surname is "+str(surcount)+" and in total they are all "+str(fullcount)+" characters long"