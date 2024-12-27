num = int(input())
stairs = list()
dp = [0] * (num)   # 0~num-1
for _ in range(num) :
    stairs.append(int(input())) #0~num-1
stairs.reverse()
if num == 1 or num == 2:
    print(sum(stairs))
else :
    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    dp[2] = dp[0] + stairs[2]
    for i in range(3, num) :
        dp[i] = max(dp[i-3]+stairs[i]+stairs[i-1],dp[i-2]+stairs[i])
    print(max(dp))
