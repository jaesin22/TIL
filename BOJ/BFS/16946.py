from signal import siginterrupt
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    # visited[x][y] = 1
    cnt = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    continue
                elif graph[nx][ny] == 0:
                    # visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
    return cnt


N, M = map(int ,input().split())
graph = []
visited = [[0] * M for _ in range(N)]
result = [[0] * M for _ in range(N)]
cnt = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            result[i][j] = 0
        elif graph[i][j] == 1:
            res = bfs(i, j)
            result[i][j] = res % 10


for x in result:
    print(x)
