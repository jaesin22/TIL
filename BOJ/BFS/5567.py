import sys
input = sys.stdin.readline

def dfs(start):
    for edge in graph[start]:
        if visited[edge] == 0:
            visited[edge] = visited[start] + 1
            dfs(edge)

N = int(input())
M = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
res = []
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = 1
dfs(1)
res = 0
for i in range(2, N + 1):
    if 0 < visited[i] < 4:
       res += 1

print(res) 