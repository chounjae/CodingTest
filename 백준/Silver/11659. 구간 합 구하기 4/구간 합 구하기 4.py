import sys
input = sys.stdin.readline


N, M = map(int,input().split())
num = list(map(int,input().split()))
midnum = [0]
for i in num :
    midnum.append(i+midnum[-1])
for i in range(M) :
    result = 0
    a, b = map(int,input().split())
    print(midnum[b]-midnum[a-1])
