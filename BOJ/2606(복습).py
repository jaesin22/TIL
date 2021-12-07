import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] * N for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

cnt = 0
def DFS(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            DFS(i)
            cnt += 1

DFS(1)
print(cnt)