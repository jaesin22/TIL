import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = 1
    distance = 0
    while queue:
        a, b, d = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    distance = d + 1
                    queue.append((nx, ny, d + 1))

    return distance

N, M = map(int, input().split())
graph = []
res = 0
for i in range(N):
    graph.append(list(map(str, input().rstrip())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            res = max(res, bfs(i, j))

print(res)