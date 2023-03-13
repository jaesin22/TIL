from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]
queue = deque()
for i in range(R):
    graph.append(list(map(str, input().strip())))
    for j in range(C):
        if graph[i][j] == 'X':
            queue.append((i, j))

visited = [[0] * C for _ in range(R)]

sea = 0
while queue:
    a, b = queue.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] == '.':
                visited[a][b] += 1
        else:
            visited[a][b] += 1
            continue

for i in range(R):
    for j in range(C):
        if visited[i][j] >= 3:
            graph[i][j] = '.'

row, col = [], []

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'X':
            row.append(i)
            col.append(j)

for i in range(min(row), max(row) + 1):
    for j in range(min(col), max(col) + 1):
        print(graph[i][j], end='')
    print()