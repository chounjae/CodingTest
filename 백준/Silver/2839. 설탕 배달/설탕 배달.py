N = int(input()) 
dp = [-1] * (N+1)
if N < 6 :
    if N ==3 or N == 5:
        print(1)
    else :
        print(-1)
else :
    dp[3] = 1
    dp[5] = 1
    for i in range(6,N+1) :
        if dp[i-3] != -1 and dp[i-5] != -1 :
            dp[i] = min(dp[i-3]+dp[3],dp[i-5]+dp[5])
        elif dp[i-5] != -1 :
            dp[i] = dp[i-5] + dp[5]
        elif dp[i-3] != -1 :
            dp[i] = dp[i-3] + dp[3] 
    print(dp[N])