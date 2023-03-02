import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, curr = heapq.heappop(queue)
        if distance[curr] < dist:
            continue
        
        for next, weight in graph[curr]:
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                prev[next] = curr
                heapq.heappush(queue, (cost, next))

    return distance

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
prev = [0] * (N+1)
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

one_dijkstra = dijkstra(1)
v1_dijkstra = dijkstra(v1)
v2_dijkstra = dijkstra(v2)

# 1부터 a까지를 one_dijkstra[v1]로 표현, a부터 b까지를 v1_dijkstra[v2]로 표현, v2에서 N까지를 v2_dijkstra[N]으로 표현
path1 = one_dijkstra[v1] + v1_dijkstra[v2] + v2_dijkstra[N] # -> 1 -> v1 -> v2-> N
path2 = one_dijkstra[v2] + v2_dijkstra[v1] + v1_dijkstra[N] # -> 1 -> v2 -> v1 -> N

res = min(path1, path2)
if res < INF:
    print(res)
else:
    print(-1)