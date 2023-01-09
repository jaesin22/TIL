import sys
input = sys.stdin.readline

N = 8
graph = []
visited = [[False] * N for _ in range(N)]
for i in range(8):
    graph.append(input().strip())

color = True # True : white, False = black
visited[0][0] = True

for i in range(N):
    for j in range(1, N):
        if visited[i][j-1] == True:
            visited[i][j] = False
        else:
            visited[i][j] = True

for i in range(N):
    for j in range(N):
        if visited[i-1][j] == True:
            visited[i][j] = False
        else:
            visited[i][j] = True

cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'F' and visited[i][j] == True:
            cnt += 1

print(cnt)
