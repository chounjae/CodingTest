import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

result = sorted(arr, key= lambda x: (x[0], x[1]))
for i in result:
    print(*i)