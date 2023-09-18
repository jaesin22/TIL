import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N, M = map(int, input().split())
visited = [0] * (N+1)
graph =[[] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)