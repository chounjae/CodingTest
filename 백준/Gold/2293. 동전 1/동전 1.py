n, k = map(int,input().split())
coins = list()
dp = [0] * (k+1) # 0~k
for _ in range(n) :
    coins.append(int(input()))


else:
    while max(coins) > k :
        coins.remove(max(coins))

    for i in coins :
        dp[i] += 1
        for j in range(i, k+1) :
            dp[j] += dp[j-i] # 코인 1개 차이 -> +1
    print(dp[k])