

n = int(input())
dice = list(map(int,input().split()))
twodice = []
threedice = []
for i in range(1,5) :
    twodice.append(dice[0]+dice[i])
    twodice.append(dice[5]+dice[i])
twodice.append(dice[1] + dice[2])
twodice.append(dice[2] + dice[4])
twodice.append(dice[3] + dice[4])
twodice.append(dice[1] + dice[3])
threedice.append(dice[0] + dice[1]+ dice[2])
threedice.append(dice[0] + dice[1]+ dice[3])
threedice.append(dice[0] + dice[2]+ dice[4])
threedice.append(dice[0] + dice[3]+ dice[4])
threedice.append(dice[5] + dice[1]+ dice[2])
threedice.append(dice[5] + dice[1]+ dice[3])
threedice.append(dice[5] + dice[2]+ dice[4])
threedice.append(dice[5] + dice[3]+ dice[4])
x = min(dice)
y = min(twodice)
z = min(threedice)
result= x*((n - 2)**2) + 4 * x *((n-1) * (n-2)) + 8 * n * y - 12*y + 4 * z
if n == 1 :
    print(sum(dice)-max(dice))
elif n == 2 :
    print(4 * y + 4* z)
else :
    print(result)