import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)
        if distance[curr] < dist:
            continue
        
        for next, weight in graph[curr]:
            cost = dist + weight
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)
print(distance[N])
