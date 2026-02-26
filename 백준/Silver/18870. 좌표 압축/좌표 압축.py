import sys
from collections import defaultdict
input = sys.stdin.readline

rep = int(input())

arr = list(map(int, input().split()))

distinctOrdered = sorted(set(arr))

rank_dict = {curr: i for i, curr in enumerate(distinctOrdered)}

result = [rank_dict[i] for i in arr]

print(*result)