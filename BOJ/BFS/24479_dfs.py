import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


cnt = 1
def dfs(start):
    global cnt
    visited[start] = cnt  
    for edge in graph[start]:
        if visited[edge] == 0:
            cnt += 1
            dfs(edge)


N, M, R = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
res = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

dfs(R)
for i in range(1, N+1):
    print(visited[i])