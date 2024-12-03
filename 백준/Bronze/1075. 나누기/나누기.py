x = int(input())
y= int(input())
compu = (x // 100) * 100
result = [0] * 2
while 1 :
    if compu % y == 0 :
        result[1] = compu % 10
        result[0] = (compu % 100) // 10
        for i in result :
            print(i,end='')
        break
    compu += 1