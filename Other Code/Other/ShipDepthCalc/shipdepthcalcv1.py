from decimal import *
speed=input("Input ultrasound speed in water")
time=input("Input time for ultrasound to travel to seabed and back")
time = Decimal(time)/2
print("The halved time is "+str(time))
distance = Decimal(speed)*Decimal(time)
print("answer is "+str(distance)+"m")
