import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

res = 0
def bfs():
    global res
    while queue:
        a, b, c, res = queue.popleft()
        for i in range(6):
            nz = a + dz[i]
            nx = b + dx[i]
            ny = c + dy[i]

            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    visited[nz][nx][ny] = visited[a][b][c] + 1
                    queue.append((nz, nx, ny, res + 1))

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                visited[i][j][k] = 1
                queue.append((i, j, k, 0))

bfs()
flag = True
for i in range(H):
    if not flag:
        break
    for j in range(N):
        for k in range(M):
            if not flag:
                break
            if graph[i][j][k] == 0:
                flag = False

if flag:
    print(res)
else:
    print(-1)