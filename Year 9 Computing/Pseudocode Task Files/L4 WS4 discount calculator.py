#L4 WS4 discount calculator

itemPrice = float(input("input item price £"))
quantity = int(input("quantity bought "))
# initialising discount desirable but not essential
discount = 0
totalCost = quantity * itemPrice
if totalCost >= 50 :
    discount  = totalCost  * 0.1
    toPay = totalCost - discount
    print ("You qualify for a discount of £", discount)
else : toPay = totalCost
print ("amount to pay is £", toPay)	

