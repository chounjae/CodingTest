import sys
input = sys.stdin.readline

n = int(input())

stairs = list(int(input()) for _ in range(n))
dp = [0] * (n)

if n > 1:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + dp[0]

    for i in range(2, n):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

else:
    dp[0] = stairs[0]        
    
print(dp[n-1])