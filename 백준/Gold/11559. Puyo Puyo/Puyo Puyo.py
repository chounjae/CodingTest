import sys
from collections import deque
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(12)]

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 인접한 같은 색 갯수 / + 터트리기 
def bfs(startY, startX, arr):
    targetColor = arr[startY][startX]
    que = deque([(startY, startX)])
    visited = [[0] * 6 for _ in range(12)] 
    cnt = 0

    while que:
        cy, cx = que.popleft()
        visited[cy][cx] = 1
        cnt += 1

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < 6 and 0 <= ny < 12 and visited[ny][nx] == 0 and arr[ny][nx] == targetColor:
                que.append((ny, nx))

    if cnt >= 4:
        for i in range(12):
            for j in range(6):
                if visited[i][j] == 1:
                    arr[i][j] = '.'    
        return True
    
    return False

result = 0 

# arr[y][x]
while True:
    isEnd = True
    for i in range(12):
        for j in range(6):
            if arr[i][j] != ".":
                if bfs(i, j, arr):
                    isEnd = False
    
    if isEnd:
        break
        
    for j in range(6):
            for i in range(11, -1, -1):
                if arr[i][j] == ".":
                    for k in range(i - 1, -1, -1):
                        if arr[k][j] != ".":
                            arr[i][j] = arr[k][j] 
                            arr[k][j] = "."       
                            break 
    result += 1
                

print(result)