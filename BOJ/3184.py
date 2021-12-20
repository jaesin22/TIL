from collections import deque

def BFS(x ,y):
    queue = deque()
    sheep = 0
    wolf = 0
    if graph[y][x] == 'o':
        sheep += 1
    elif graph[y][x] == 'v':
        wolf += 1
    queue.append((x, y))
    graph[y][x] = '#'

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < C and 0 <= ny < R:
                if graph[ny][nx] != '#':
                    if graph[ny][nx] == 'o':
                        sheep += 1
                    elif graph[ny][nx] == 'v':
                        wolf += 1
                    
                    queue.append((nx, ny))
                    graph[ny][nx] = '#'
    if sheep > wolf:
        res[0] += sheep
    else:
        res[1] += wolf

R, C = map(int, input().split())
graph = []
res = [0, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(R):
    graph.append(list(map(str, input())))


for i in range(R):
    for j in range(C):
        if graph[i][j] != '#':
            BFS(j, i)

print(*res)