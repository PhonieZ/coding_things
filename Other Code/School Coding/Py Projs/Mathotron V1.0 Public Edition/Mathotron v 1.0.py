


import time
while 1 == 1:
    username = input("Username:")
    print("Hello")
    print(username)
    f = open('User_Data.txt','a')
    f.write('\n' + '')
    f.write('\n' + '')
    f.write('\n' + '')
    f.write('\n' + 'user:')
    f.write('\n' + username )
    f.close()
    mode = input("select a mode, plus , minus , times or divide")
    if mode == "plus":
        print("Addition mode selected")
        Num1 = input("Num1:")
        print(Num1)
        Num2 = input("Num2:")
        print(Num2)
        ans = int(Num1) + int(Num2)
        print(ans)
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    elif mode == "minus":
        print("Subtraction mode selected")
        Num1 = input("Num1:")
        print(Num1)
        Num2 = input("Num2:")
        print(Num2)
        ans = int(Num1) - int(Num2)
        print(ans)
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    elif mode == "times":
        print("Multiplication mode selected")
        Num1 = input("Num1:")
        print(Num1)
        Num2 = input("Num2:")
        print(Num2)
        ans = int(Num1) * int(Num2)
        print(ans)
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    elif mode == "divide":
        print("Divison mode selected")
        Num1 = input("Num1:")
        print(Num1)
        Num2 = input("Num2:")
        print(Num2)
        ans = int(Num1) / int(Num2)
        print(ans)
        f = open('User_Data.txt','a')
        f.write('\n' + 'Type:')
        f.write('\n' + mode )
        f.write('\n' + 'Num1:')
        f.write('\n' +  str(Num1) )
        f.write('\n' + 'Num2:')
        f.write('\n' +  str(Num2) )
        f.write('\n' + 'ans:')
        f.write('\n' +  str(ans) )
        f.close()
    else:
        print("invalid option,rebooting")
        time.sleep(3)



    
    
    


