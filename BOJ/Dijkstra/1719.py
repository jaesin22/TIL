import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)
        
        if dist > distance[curr]:
            continue       
        
        for next, weight in graph[curr]:
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                answer[next-1][start-1] = curr
                heapq.heappush(queue, (cost, next))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(N+1):
    dijkstra(i)

for i in range(N):
    for j in range(N):
        if i == j:
            print('-', end = ' ')
        else:
            print(answer[i][j], end = ' ')
    print()