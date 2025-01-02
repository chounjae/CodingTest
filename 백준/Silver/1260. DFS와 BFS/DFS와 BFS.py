from collections import deque


def DFS(graph,V,visited) :
    visited[V] = True
    print(V,end=' ')
    for i in graph[V] :
        if not visited[i] :
            DFS(graph,i,visited)
  
def BFS(graph,V,visited) :  
    que = deque([V])
    visited[V] = True
    while que :
        temp = que.popleft()
        print(temp,end=' ')
        for i in graph[temp] :
            if not visited[i] :
                que.append(i)
                visited[i] = True
    
N , M , V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
for i in range(1, N+1) :
    graph[i].sort()
visited = [False] * (N+1)
DFS(graph,V,visited)
print('')
for i in range(N+1) :
    visited[i] = False
BFS(graph,V,visited)