import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e10)
dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y, L, R))
    visited[x][y] = 1
    while queue:
        a, b, L_cnt, R_cnt  = queue.popleft()
        # 상, 하
        for i in range(2):
            nx = a + dx[i]
            ny = b + dy[i]
            while 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                queue.append((nx, ny, L_cnt, R_cnt))
                nx, ny = nx + dx[i], ny + dy[i]
        # 좌
        if L_cnt > 0:
            nx, ny = a + dx[2], b + dy[2]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny, L_cnt-1, R_cnt))
        #우
        if R_cnt > 0:
            nx, ny = a + dx[3], b + dy[3]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny, L_cnt, R_cnt-1))


N, M = map(int, input().split())
L, R = map(int, input().split())
cnt = 1
graph = []
visited = [[0] * M for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

x, y = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            x, y = i, j
            graph[i][j] = 0
            break

bfs(x, y)
print(cnt)