import sys
from collections import deque

graph = []

n, m = map(int, input().split())
for x in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []
cnt = 0


def bfs(x, y):
    global cnt
    queue = deque()

    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] != 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                graph[nx][ny] = 3
                cnt += 1
        res.append(cnt)
        cnt = 0


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] != 0:
            bfs(i, j)

res.sort()
print(res)
