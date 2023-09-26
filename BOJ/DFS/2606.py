N = int(input())
M = int(input())

def dfs(v):
    global count
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            count += 1

graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
count = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)

print(count)