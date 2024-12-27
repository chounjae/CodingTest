num = int(input())
red = list()
green = list()
blue = list()
dpr = [0] * num
dpg = [0] * num
dpb = [0] * num

for _ in range(num) :
    r,g,b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)
dpb[0] = blue[0]
dpg[0] = green[0]
dpr[0] = red[0]
dpb[1] = blue[1] + min(red[0],green[0])
dpg[1] = green[1] + min(blue[0],red[0])
dpr[1] = red[1] + min(blue[0],green[0])
if num <= 2:
    print(min(dpg[num-1],dpr[num-1],dpb[num-1]))
else :
    for i in range(2,num) :
        dpr[i] = min(dpg[i-1]+red[i],dpb[i-1]+red[i])
        dpb[i] = min(dpg[i-1]+blue[i],dpr[i-1]+blue[i])
        dpg[i] = min(dpr[i-1]+green[i],dpb[i-1]+green[i])
    print(min(dpr[num-1],dpb[num-1],dpg[num-1]))