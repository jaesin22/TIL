from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] * n for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [] * (n+1)
cnt = 0

def bfs(v):
    global cnt
    queue = deque()
    queue.append((v))
    visited[v] = 1

    while queue:
        x = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                queue.append(i)
                visited[v] = 1


bfs(1)
print(cnt)