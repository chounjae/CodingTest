import sys
input = sys.stdin.readline


N, M = map(int,input().split())
bags = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (M+1)

for i, j in bags :
    for k in range(M,0,-1) :
        if k >= i :
            dp[k] = max(dp[k],dp[k-i]+j,j)
print(max(dp))