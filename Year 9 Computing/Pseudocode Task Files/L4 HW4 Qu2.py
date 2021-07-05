#L4 HW4 Qu2.py
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input ("Enter m for multiply, d for divide, \
f for floor division, r for remainder: ")
       
if op == "m":
    result = a*b
elif op == "d":
    result = a/b
elif op == "f":
    result = a//b
elif op == "r":
    result = a%b            
else:
    result = "Error - invalid operation entered"
print("Result: ", result)
