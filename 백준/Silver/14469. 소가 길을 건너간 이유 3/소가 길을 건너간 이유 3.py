import sys
input = sys.stdin.readline

N = int(input())
cows = []
for i in range(N) :
    w, v = map(int,input().split())
    cows.append((w,v))
cows.sort()
time = 0
for i in range(N) : 
    if time < cows[i][0] :
        time = cows[i][0]
    time += cows[i][1]
print(time)