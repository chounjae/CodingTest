import sys
input = sys.stdin.readline
INF = int(1e9)

N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
dp = [INF] * (K+1)

for coin in coins :
    for i in range(1, K+1) :  # i가 target
        if i == coin :
            dp[i] = 1 
        elif i > coin :
            dp[i] = min(dp[i-coin]+1,dp[i])
if dp[K] == INF :
    print(-1)
else : 
    print(dp[K])