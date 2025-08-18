import sys

input = sys.stdin.readline

before = 1  
after = 2  

n = int(input())

for i in range(2, n):
    temp = before + after
    before = after
    after = temp % 15746

if(n == 1):
    print(before)
else:
    print(after)

