import sys
input = sys.stdin.readline
N = int(input())
cases = []
for _ in range(N) :
    cases.append(int(input()))
cases.sort()
result = 0
for i in range(N) :
    result += abs(cases[i] - (i + 1))
print(result)