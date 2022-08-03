list = [18,19,5,9,21,12,1,3,15,2,17,33,55,24,35,31,37,51,64,41,29,45,59,81,87]
i = 0
num = 0
divisor = 2
listnum = len(list)
while i < listnum+1:
    if (num/divisor).is_integer():
        i = i + 1
        divisor = 2
        num = list[i]
        continue
    else:
        while divisor < num+1:
            if (num/divisor).is_integer():
                i=i+1
                divisor=2
                num=list[i]
                continue
            else:
                if divisor == num:
                    print(num)
                    divisor = 2
                    i = i+1
                    num = list[i]
                    continue
                else:
                    divisor = divisor + 1
print("done!")
