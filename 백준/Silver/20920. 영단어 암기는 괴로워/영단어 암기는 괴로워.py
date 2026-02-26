import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int,input().split())
arr = []

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        arr.append(word)

counts = Counter(arr)

ordered = sorted(arr, key=lambda x: (-counts[x], -len(x), x))
result = list(dict.fromkeys(ordered))

for i in result:
    print(i)