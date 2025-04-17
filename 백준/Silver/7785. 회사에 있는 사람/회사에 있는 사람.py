import sys

input = sys.stdin.readline

n = int(input())
nowExist = set()

for i in range(n):
    a, b = input().split()
    if b == 'enter' :
        nowExist.add(a)
    elif b == 'leave' :
        nowExist.remove(a)

for j in sorted(nowExist, reverse=True):
    print(j)