import sys

input = sys.stdin.readline

repeat = int(input())

c = list()

for _ in range(repeat):
    a, b = input().split()
    c.append([int(a), b])

c.sort(key=lambda x: (x[0]))

for i in c:
    print(i[0], i[1])