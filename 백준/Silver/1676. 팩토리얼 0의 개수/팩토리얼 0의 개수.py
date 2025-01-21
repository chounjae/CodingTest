import sys
input = sys.stdin.readline

n = int(input())
fac = 1
for i in range(1,n+1) :
    fac *= i
spare = 0
cnt = 0
while 1 :
    spare = fac % 10 
    fac = fac // 10
    if spare == 0 :
        cnt += 1
    else :
        print(cnt) 
        break