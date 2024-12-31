num = int(input())
cases = list(map(int, input().split()))
dp = [0] * (num)
dp[0] = cases[0]
for i in range(1,num) :
    dp[i] = max(cases[i], dp[i-1] + cases[i])
print(max(dp))