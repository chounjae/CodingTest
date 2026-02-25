from collections import defaultdict, Counter

n, m  = map(int, input().split())


arr = list(map(int, input().split()))

order = {}

for i, x in enumerate(arr):
    if x not in order:
        order[x] = i

counts = Counter(arr)

sorted_arr = sorted(counts.items(), key=lambda x: (-x[1], order[x[0]]))

result = []
for val, cnt in sorted_arr:
    result.extend([val] * cnt)

print(*result)