while 1 == 1:
    timtable = input("Type A Number For Times Tables")
    upto = input("Type In The Number To Go Up To")
    times = 0
    while float(times) < float(upto)+1 :
        print(times,"x",timtable,"=",float(timtable)*float(times))
        times = times + 1

