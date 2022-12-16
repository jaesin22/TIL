import sys
input = sys.stdin.readline

def dfs(node):
    for n in graph[node]:
        if visited[n] == 0:
            visited[n] = visited[node]+1
            dfs(n)

T = int(input())            
for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(1, N + 1):
        v = int(input())
        graph[i].append(v)
    visited = [0] * (N + 1)
    dfs(1)
    print(visited[N] if visited[N] > 0 else 0)