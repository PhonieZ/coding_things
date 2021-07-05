import time
"""
values
"""
i = 10
ctemp = 0
cplus = 0
coreon =0
coolantactive = 0
fanactive = 0
credits = 0
earning = 3
experiments = 0
tests = 15
print("The ship is on standby, the core is offline,")
corereq = input("input y to actvate the core, n to decline")
if corereq == 'y':
    print("Core Start Procedure Activated")
    time.sleep(1)
    print("Core Chamber is being sealed")
    time.sleep(2)
    print("Core Chamber Sealed")
    print("Activating Core Compression")
    time.sleep(1)
    print("inserting compound[REDACTED]")
    time.sleep(3)
    print("Compressing")
    time.sleep(5)
    print("Core is online.activating pressure reactor")
    time.sleep(3)
    coreon = 1
    cplus = 5
    print('power output is at ', cplus, 'UW')

    while 1==1:
        time.sleep(1)
        ctemp = ctemp +cplus
        print (ctemp)

    pass
else:
     print("Core Activation Declined,Initiating Self Destruct")


     while i >0:
        time.sleep(1)
        print('Detonating in', i,)
        i=i - 1
     pass
     print("Lifesigns at facility[READCTED] is 0,shutting down terminal...")
     pass













