import sys
input = sys.stdin.readline
from collections import deque

# 섬 구분 bfs
def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    graph[x][y] = cnt

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = cnt
                    queue.append((nx, ny))


def seabfs(z):
    global res
    dist = [[-1] * N for _ in range(N)] # 거리가 저장될 배열
    queue = deque()
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == z:
                queue.append((i, j))
                dist[i][j] = 0
    
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:

                # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
                if graph[nx][ny] > 0 and graph[nx][ny] != z:
                    res = min(res, dist[a][b])
                    return

                # 바다를 만나면 dist를 1씩 늘린다.
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[a][b] + 1
                    queue.append((nx, ny))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * N for _ in range(N)]

res = 10000000
cnt = 1

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == 1:
            bfs(i, j)
            cnt += 1

for i in range(1, cnt):
    seabfs(i)

print(res)