import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
one, two = 0, 0
def bfs(x, y):
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == graph[a][b]:
                        visited[nx][ny] = 1
                        queue.append((nx,ny))


N = int(input())
visited = [[0] * N for _ in range(N)]
graph = [list(map(str, input().rstrip())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            one += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            two += 1

print(one, two)