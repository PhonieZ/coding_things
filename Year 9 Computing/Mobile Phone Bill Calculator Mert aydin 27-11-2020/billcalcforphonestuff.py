#mobile phone cost calc
#also the prints for mins and texts is for debug
name = ""
carrier = ""
info = False
def send():
    main()
def main():
    global name
    global carrier
    global info
    if info == False:
        name = input("What Is Your Name?")
        carrier = input("What is your mobile phone carrier "+name+"?")
        print(name)
        print(carrier)
        info = True
        calcstuff()
    else:
        calcstuff()
def calcstuff():
        global name
        global carrier
        global info
        mins=input("How many minutes have you used this month "+name+"?")
        print(mins)
        try:
            mins = float(mins)*0.10
            print(str(mins))
        except:
            print("Invalid input")
            send()
        texts=input("How many texts have you sent this month "+name+"?")
        print(texts)
        try:
            texts = float(texts)*0.05
            print(str(texts))
        except:
            print("Invalid input")
            send()
        sum = float(texts) + float(mins)
        vat = float(sum)+float(sum/100*20)
        print("Your bill without vat is: £"+str(sum)+" with vat it is: £"+str(vat))
send()
