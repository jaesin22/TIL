import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [0] * (V+1)
graph = [[] for _ in range(V+1)]
res = 0
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


cnt = 0
queue = []
heapq.heappush(queue, (0, 1))

while queue:
    c, b = heapq.heappop(queue)
    if cnt == V:
        break
    
    if visited[b] == 0:
        visited[b] = 1
        res += c
        cnt += 1
        for i in graph[b]:
            heapq.heappush(queue, i)

print(res)