import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx =  a + dx[i]
            ny =  b + dy[i]

            if nx >= N:
                nx = 0
            elif nx <= -1:
                nx = N-1

            if ny >= M:
                ny = 0
            elif ny <= -1:
                ny = M-1

            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and graph[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)