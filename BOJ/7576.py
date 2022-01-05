from collections import deque
M, N = map(int, input().split())

graph = []
for x in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

visited = [[0] * M for _ in range(N)]

def BFS():
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1
                queue.append([nx, ny])


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

BFS()
isTrue = False
result = -2
for i in graph:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)