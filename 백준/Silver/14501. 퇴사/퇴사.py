N = int(input())

caseT = [0] * (N+2)
caseP = [0] * (N+2)
dp = [0] * (N+2)
for i in range(1,N+1) :
    T,P = map(int,input().split())
    caseT[i] = T
    caseP[i] = P

for i in range(N,0,-1) :
    if caseT[i] < N+2-i :
        dp[i] = max(caseP[i],dp[i+caseT[i]]+caseP[i],dp[i+1])
    else :
        dp[i] = dp[i+1]
print(max(dp))