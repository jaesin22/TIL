import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] * (N+1)]
distance = [INF] * (N+1)
for i in range(M):
    u, m, v = map(int,input().split())
    graph[u].append((m, v))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

for i in range(N):
    dijkstra(i)



