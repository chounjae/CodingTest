import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

counts = Counter(n_arr)

result = [counts[m_arr[i]] for i in range(m)]

print(*result)