import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

n = int(input())
results = []

for _ in range(n):
    m = int(input())
    clothes = defaultdict(int)
    for _ in range(m):
        a, b = input().split()
        clothes[b] += 1

    result = 1
    for i in clothes.values():
        result *= (i + 1)
    
    result -= 1
    results.append(result)

for i in results:
    print(i)

    
        
    