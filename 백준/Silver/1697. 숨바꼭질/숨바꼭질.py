from collections import deque
N, K = map(int, input().split())

#-1 or +1 or *2 
record = 100001 * [0]
que = deque([N])
while 1 :
    temp = que.popleft()
    if temp == K :
        print(record[temp])
        break
    for i in (temp-1,temp+1,temp*2) :
        if 0<= i <100001 and record[i] == 0 :
            record[i] = 1 + record[temp]
            que.append(i)