import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())
distance = [INF] * (N+1)
graph = [[] for i in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, curr = heapq.heappop(queue)
        if dist > distance[curr]:
            continue

        for next, weight in graph[curr]:
            cost = dist + weight # weight는 현재의 가중치
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))
    
    print(distance[end])

dijkstra(start, end)