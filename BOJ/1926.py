import queue
import sys
from collections import deque

n, m = map(int, input().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

res = []
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = 0
    cnt = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = 0
                    cnt += 1

    res.append(cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

res.sort()
print(len(res))
if len(res) == 0: print(0)
else: print(res[-1])