from collections import deque


def DFS(graph,V,visited,result) :
    visited[V] = True
    result.append(V)
    for i in graph[V] : 
        if not visited[i] :
            DFS(graph,i,visited,result)
    return result
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M) :
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
for i in range(1, N+1) :
    graph[i].sort()
result = list()
a = DFS(graph,1,visited,result)
print(len(a)-1)
