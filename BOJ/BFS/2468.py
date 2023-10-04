from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(cnt):
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

cnt = 1

for i in range(N):
    for j in range(N):
        bfs(i, j, cnt)
        cnt += 1
