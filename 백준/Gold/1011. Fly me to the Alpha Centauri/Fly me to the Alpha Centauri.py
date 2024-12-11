
rep = int(input())

for _ in range(rep) :
    x, y = map(int,input().split())
    f = [1,2]
    i = 1
    stop = 1
    while stop == 1 :
        i += 1
        f.append(i**2)
        if (y-x) <= 3 :
            print(y-x)
            stop = 0
        elif (y-x) <= f[-1] :

            z = (f[-1] - f[-2])
            com = z // 2
            if (y-x) > f[-2] + com :
                print((len(f)-1) * 2 - 1)
                stop = 0
            else :
                print((len(f)-1) * 2 - 2)
                stop = 0
        

