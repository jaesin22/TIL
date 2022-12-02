import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = []
arr = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for x in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]
S, X, Y = map(int, input().split())

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            arr.append([graph[i][j], i, j, 0])
            visited[i][j] = 1

arr.sort()
queue = deque(arr)

def bfs():
    while queue:
        virus, a, b, c  = queue.popleft()

        if c == S:
            return

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = graph[a][b]
                    queue.append((virus, nx, ny, c + 1))
                

bfs()
print(graph[X-1][Y-1])