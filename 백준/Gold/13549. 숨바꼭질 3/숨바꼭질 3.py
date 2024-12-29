from collections import deque
N, K = map(int,input().split())
limit = 100000
visit = [-1] * (limit+1)
visit[N] = 0
que = deque([N])
if N >= K :
     print(N-K)
else :
    while 1 :
        temp = que.popleft()
        if temp == K :
            break
        if (temp * 2) <= limit and visit[temp*2] == -1 :
            que.append(temp*2)
            visit[temp*2] = visit[temp]
        for i in (temp-1, temp+1) :
            if i >= 0 and i <= limit and visit[i] == -1 :
                visit[i] = visit[temp] + 1
                que.append(i)
        
    print(visit[K])