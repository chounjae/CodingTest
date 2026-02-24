import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

test_case = int(input())
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
            dfs(nx, ny)


for _ in range(test_case):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    result.append(count)


for i in result:
    print(i)