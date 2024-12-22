from collections import deque
N = int(input())
record = 1000001 * [0]
que = deque([N])

while 1 :
    temp = que.popleft()
    if temp == 1 :
        print(record[temp])
        break
    if temp % 2 == 0 and record[temp//2] == 0:
        record[temp//2] = record[temp] + 1
        que.append(temp//2)
    if temp % 3 == 0 and record[temp//3] == 0:
        record[temp//3] = record[temp] + 1
        que.append(temp//3)
    if record[temp-1] == 0 :
        record[temp-1] = record[temp] +1
        que.append(temp-1)