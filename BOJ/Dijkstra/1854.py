import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    queue = []
    distance[start][0] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)

        for next, weight in graph[curr]:
            cost = dist + weight
            if cost < distance[next][K-1]:
                distance[next][K-1] = cost
                before[next] = curr
                distance[next].sort()
                heapq.heappush(queue, (cost, next))


N, M, K = map(int, input().split())
distance = [[INF] * K for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
before = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(1)

for i in range(1, N + 1):
    if distance[i][K-1] == INF:
        print(-1)
    else:
        print(distance[i][K-1])