from collections import deque
N, M = map(int, input().split())

graph = [list(input().strip()) for _ in range(M)]

visited = [[0] * N for _ in range(M)]

white, blue = 0, 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
def BFS(x, y):
    cnt = 1
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and graph[a][b] == graph[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
            
    return cnt

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            res = BFS(i, j)
            if graph[i][j] == 'W':
                white += res ** 2
            else:
                blue += res ** 2

print(white, blue)

