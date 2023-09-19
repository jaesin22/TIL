import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(v):
    global cnt
    visited[v] = 1
    res[v] = cnt

    graph[v].sort()    
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
res = [0] * (N+1)
cnt = 1
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)
for i in range(1, N+1):
    print(res[i])