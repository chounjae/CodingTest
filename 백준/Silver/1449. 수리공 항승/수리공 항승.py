import sys
input = sys.stdin.readline

N,L = map(int,input().split())

spots = list(map(int,input().split()))
spots.sort()
tape = N
temp = spots[0]
for i in range(1, N) :
    if spots[i] - temp + 1 <= L :
        tape -= 1
    else :
        temp = spots[i]
print(tape)