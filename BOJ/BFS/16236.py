import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
INF = int(1e9)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
baby = 2
x, y = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

def search():
    queue = deque()
    queue.append((x, y))
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if baby >= graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[a][b] + 1
                    queue.append((nx, ny))
    
    return visited 


def check(visited):
    a, b = 0, 0
    dist = INF
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and 1 <= graph[i][j] < baby:
                if visited[i][j] < dist:
                    dist = visited[i][j]
                    a, b = i, j
    
    if dist == INF:
        return False
    else:
        return a, b, dist

ans = 0
cnt = 0

while True:
    res = check(search())

    if not res:
        print(ans)
        break
    else:
        x, y = res[0], res[1]
        ans += res[2]
        graph[x][y] = 0
        cnt += 1
    
    if cnt >= baby:
        baby += 1
        cnt = 0