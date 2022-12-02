from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, n+1):
    edges[i].sort()

def dfs(edges, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in edges[v]:
        if not visited[i]:
            dfs(edges, i, visited)

def bfs(edges, v, visited):
    queue = deque([v])

    visited[v] = True
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in edges[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)





visited = [False] * (n+1)
dfs(edges, v, visited)
print()
visited = [False] * (n+1)
bfs(edges, v, visited)


