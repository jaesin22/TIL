import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for i in range(N + 1)]

for _ in range(M):
    u, m, v = map(int, input().split())
    graph[u].append((m, v))

def dijkstra(start):
    distance = [INF] * (N+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, curr = heapq.heappop(queue)
        
        if dist > distance[curr]:
            continue
        
        for next, weight in graph[curr]:
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))
    
    return distance

res = 0
back = dijkstra(X)
for i in range(1, N+1):
    go = dijkstra(i)
    res = max(res, go[X] + back[i]) # go[X] = X 번 마을까지의 최단 경로, back[i] = 나머지 다른 마을로의 모든 최단경로


print(res)