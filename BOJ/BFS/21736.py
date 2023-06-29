from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    global res
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 'O':
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                    if graph[nx][ny] == 'P':
                        res += 1
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                

N, M = map(int, input().split())

visited = [[0] * M for _ in range(N)]
graph = [list(map(str, input().rstrip())) for _ in range(N)]
res = 0
x, y = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            bfs(i, j)
            break

if not res:
    print('TT')
else:
    print(res)
