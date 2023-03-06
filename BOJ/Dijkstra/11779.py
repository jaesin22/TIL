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
            if cost < distance[next]:
                distance[next] = cost
                visited[next] = visited[curr] + [next]
                heapq.heappush(queue, (cost, next))

    return distance


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b , c))

start, end = map(int, input().split())
visited = [[i] for i in range(N + 1)]
res = dijkstra(start)
print(res[end])
print(len(visited[end]))
print(*visited[end])