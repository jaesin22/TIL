import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    graph[nx][ny] = graph[a][b] + 1
                    queue.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] > 0:
                graph[i][j] = -1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
N, M = map(int, input().split())
graph = []
visited = [[0] * M for _ in range(N)]
queue = deque()
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 2:
            queue.append((i, j))
            graph[i][j] = 0
            visited[i][j] = 1

bfs()
print(graph)
for i in range(N):
    for j in range(M):
        print(graph[i][j], end = ' ')
    print()