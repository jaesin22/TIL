from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 0
    while queue:
        node = queue.popleft()
        d = [node-1, node+1]
        if graph[node]:
            d += graph[node]
        for i in d:
            if (1 <= i <= N) and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[node] + 1
            if i == E:
                return visited[i]

N, M = map(int, input().split())
S, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = bfs(S)
print(cnt)