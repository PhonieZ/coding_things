#L4 WS4 Tax Calculator.py
#errors pointed out...
salary = int(input("Please enter your annual salary: £"))) ###bug1: extra closing parenthesis

if salary < 30000 ###bug2: Missing colon
#Salaries under 30000 are taxed at 20%
    tax = salary * 0.2
elif salary >= 30000:
#Salaries over 30000 are taxed at 40% for anything over 30000
    salary = salary - 30000
tax = salary * 0.4 + 6000 ###bug3: No indentation
else:
#Salaries over 150000 are taxed at 45% for anything over 150000
    salary = salary - 150000
    tax = salary * 0.45 + 6400 + 48000

    
print("Earnings of £",salray,"will attract taxes of £",round(tax,2)) ###bug4: "salray" variable misspelled

input("Press ENTER to quit")

###bug5: logic error - 'else' part will never execute since all
###salaries will be over 30000 in 'elif' part if they are not
###under 30000 in 'if' part.

