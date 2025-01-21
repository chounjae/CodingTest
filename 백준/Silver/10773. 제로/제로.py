import sys
input = sys.stdin.readline

n = int(input())
num = list()

for i in range(n) :
    k = int(input())
    if k == 0 :
        num.pop()
    else :
        num.append(k)
print(sum(num))