import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = []

for x in range(N):
    graph.append(input())

dy =[-1,1,0,0]
dx = [0,0,-1,1]
def bfs(x, y):
    distance = 0
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = 1
    
    while queue:
        a, b, d = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 'L':
                visited[nx][ny] = 1
                queue.append([nx, ny, d+1])
                distance = d + 1
    return distance


cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            print(cnt)
            cnt = max(cnt, bfs(i, j))

print(cnt)