import sys
input = sys.stdin.readline

repeat = int(input())

graph = [list(map(int, input().strip())) for _ in range(repeat)]

count_list = []

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(start, graph):
    x, y = start
    graph[x][y] = 0
    count = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < repeat and 0 <= ny < repeat and graph[nx][ny] == 1:
            count += dfs((nx, ny), graph)

    return count

for i in range(repeat):
    for j in range(repeat):
        if graph[i][j] == 1:
            
            count_list.append(dfs((i, j), graph))

print(len(count_list))
count_list.sort()
for count in count_list:
    print(count)