from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)
def dyscra(graph,start) :
    
    distance = [INF] * (V+1)  
    q = list()
    heappush(q,(0,start))   # graph 저장은 (node,dist)
    distance[start] = 0

    while q :
        dist,nod = heappop(q)  # dist와 nod 는 전에 했던 거리와 연결 노드
        for i in graph[nod] :  
            temp = dist + i[1] # i[1] 은 dist
            if temp < distance[i[0]] :
                distance[i[0]] = temp
                heappush(q,(temp,i[0]))
    return distance

V, E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) 

result = dyscra(graph,K)

for i in range(1,V+1) :
    if result[i] == INF :
        print('INF')
    else :
        print(result[i])