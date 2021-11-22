from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())

graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
cnt = 0

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)