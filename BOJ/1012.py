import queue
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    queue = deque()
    graph[x][y] = 0
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

for x in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

