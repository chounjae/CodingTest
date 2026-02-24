import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(maze):
    queue = deque([(0, 0, 1)])
    maze[0][0] = 0

    while queue:
        x, y, cnt = queue.popleft()

        if x == n-1 and y == m-1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                    maze[nx][ny] = 0  
                    queue.append((nx, ny, cnt + 1))

print(bfs(maze))