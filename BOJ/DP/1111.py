import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b  = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx == -1:
                nx = N-1
            elif ny == -1:
                ny = M-1
            
        if visited[nx][ny] == 0  and graph[nx][ny] == 0:
            queue.append((nx, ny))
            visited[nx][ny] = 1


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)
            cnt += 1

print(cnt)