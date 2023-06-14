import sys
from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
# L, R, U, D

def escape(x, y):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    visited[x][y] = 1
    queue.append((x, y))
    
    while queue:
        a, b = queue.popleft()
        nx, ny = 0, 0
        if graph[a][b] == 'L':
            nx = a + dx[0]
            ny = b + dy[0]
        elif graph[a][b] == 'R':
            nx = a + dx[1]
            ny = b + dy[1]
        elif graph[a][b] == 'U':
            nx = a + dx[2]
            ny = b + dy[2]
        elif graph[a][b] == 'D':
            nx = a + dx[3]
            ny = b + dy[3]
        
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
            else:
                return False
            
        elif 0 > nx or 0 > ny or nx >= N or ny >= M:
            return True
    
    return False


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input().rstrip()))

res = 0
for i in range(N):
    for j in range(M):
        if escape(i, j):
            res += 1

print(res)