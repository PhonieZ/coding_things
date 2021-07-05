#L4 WS4 Tax CalculatorBUGS.py
#Tax Calculator program  with 5 bugs

salary = int(input("Please enter your annual salary: Â£"))

if salary < 30000:
#Salaries under 30000 are taxed at 20%
    tax = salary * 0.2
elif salary >= 30000:
#Salaries over 30000 are taxed at 40% for anything over 30000
    salary = salary - 30000
    tax = salary * 0.4 + 6000
print("Earnings of Â£",salary,"will attract taxes of Â£",round(tax,2))
input("Press ENTER to quit")

