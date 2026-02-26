import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

counts = Counter(n_arr)
result = [0] * m

for i in range(m):
    if m_arr[i] in counts.keys():
        result[i] = counts[m_arr[i]]
        
print(*result)
