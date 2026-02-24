import sys
from collections import deque as dq
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for j in range(1, n+1) :
    graph[j].sort()

def dfs(start, graph, visited) :
    visited[start] = True
    print(start, end=' ')
    for i in graph[start] :
        if not visited[i]:
            dfs(i, graph, visited)
        
def bfs(start, graph, visited) :
    visited[start] = True
    queue = dq([start])

    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                visited[i] = True
                queue.append(i)

visited = [False] * (n+1)
dfs(v, graph, visited)
print()
visited = [False] * (n+1)
bfs(v, graph, visited)
