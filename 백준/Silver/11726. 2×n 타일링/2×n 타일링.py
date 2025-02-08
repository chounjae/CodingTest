dp = [0] * 1002

dp[1] = 1
dp[2] = 2

n = int(input())

if n > 2 :
    for i in range(3,n+1) :
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n] % 10007)
else :
    print(n)