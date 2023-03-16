import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    global c, d
    queue = deque()
    sheep, wolf = 0,0
    if graph[x][y] == 'o':
        sheep += 1
    elif graph[x][y] == 'v':
        wolf += 1
    
    queue.append((x, y))
    graph[x][y] = '#'
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != '#':
                    if graph[nx][ny] == 'o':
                        sheep += 1
                    elif graph[nx][ny] == 'v':
                        wolf += 1
                    
                    graph[nx][ny] = '#'
                    queue.append((nx, ny))
                    
    if sheep > wolf:
        c += sheep
    else:
        d += wolf

N, M = map(int, input().split())
graph = []
visited = [[0] * M for _ in range(N)]
c, d = 0,0
for i in range(N):
    graph.append(list(map(str, input().rstrip())))



for i in range(N):
    for j in range(M):
        if graph[i][j] != '#':
            bfs(i, j)

print(c, d)