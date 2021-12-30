import sys

R, C = map(int, sys.stdin.readline().split())

graph = []
visited = [[0] * C for _ in range(R)]

wolf = 0
sheep = 0

for x in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global w, s
    visited[x][y] = 1

    if graph[x][y] == 'v':
        w += 1
    elif graph[x][y] == 'k':
        s += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and visited[nx][ny] == 0:
            dfs(nx, ny)

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visited[i][j] == 0:
            w = 0
            s = 0
            dfs(i, j)
            if w >= s:
                s = 0
            else:
                w = 0
            
            wolf += w
            sheep += s

print(sheep, wolf)