import sys

M, N = map(int, sys.stdin.readline().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))


dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
visited = [[0] * N for i in range(M)]
cnt = 0

def bfs(x, y):
    queue = [[x, y]]

    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]

        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx, ny])

for x in range(M):
    for y in range(N):
        if not visited[x][y] and graph[x][y]:
            visited[x][y] = 1
            bfs(x, y)
            cnt += 1


print(cnt)
