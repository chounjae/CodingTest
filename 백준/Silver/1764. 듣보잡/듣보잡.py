import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())

no_hear = set(input().strip() for _ in range(n))
no_look = set(input().strip() for _ in range(m))

no_hear_and_look = no_hear & no_look

result = list(no_hear_and_look)

print(len(result))

for i in sorted(result) :
    print(i)