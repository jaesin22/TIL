import sys
from collections import deque
input = sys.stdin.readline

visited = [[0] * 6 for _ in range(12)]
graph = []
for _ in range(11):
    graph.append(list(map(int, input().rstrip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    cnt = 0

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if graph[a][b] == graph[nx][ny]:
                    queue.append((nx, ny))
                    cnt += 1

for i in range(11):
    for j in range(5):
        if graph[i][j] != '.':
            bfs(i, j)