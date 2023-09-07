import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    count += 1
                    queue.append((nx, ny))

    return count


N = int(input())
visited = [[0] * N for _ in range(N)]
graph = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = 1
res = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            res.append(bfs(i, j))
            cnt += 1

print(len(res))
res.sort()
for i in res:
    print(i)
