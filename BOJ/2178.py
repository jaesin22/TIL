import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
N, M = map(int, input().split())
graph = []
for x in range(N):
    graph.append(list(map(str, input().rstrip())))

 
visited = [[False] * M for _ in range(N)]
cnt = 0
def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y, 1))
    visited[x][y] = True
    graph[x][y] = 0

    while queue:
        a, b, c = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and graph[nx][ny] == '1':
                visited[nx][ny] = True
                graph[nx][ny] = 0
                queue.append((nx, ny, c+1))
    print(c)

for i in range(N):
    for j in range(M):
        if graph[i][j] == '1' and visited[i][j] == False:
            bfs(i, j)
            