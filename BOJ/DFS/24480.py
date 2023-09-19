import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def dfs(v):
    global cnt
    visited[v] = 1
    # 4번은 2번째 방문, 3번은 3번째 방문, 2번은 4번째 방문
    # 카운트는 1씩 증가하는데.. 2번째일 때, 4번을 방문하므로, answer[4] = 2와 같다.
    res[v] = cnt

    graph[v].sort(reverse=True)

    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
            





N, M, R = map(int, input().split())
res = [0] * (N+1)
cnt = 1
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)

for i in range(1, N+1):
    print(res[i])