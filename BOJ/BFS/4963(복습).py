from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1, 1, -1, 1, -1] #상하좌우+대각선
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()

        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny)) 

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    cnt = 0
    visited = [[0] * w for _ in range(h)]
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)


