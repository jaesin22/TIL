from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

graph = [[] * N for i in range(N+1)]

for x in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
visited = [0] * (N+1) # 방문체크 

def bfs(node):
    queue = deque([node])
    while(queue):
        n = queue.popleft()
        for x in graph[n]:
            if visited[x] == 0:
                queue.append(x)
                visited[x] = 1

cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)