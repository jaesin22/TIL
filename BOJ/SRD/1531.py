N, M = map(int, input().split())
graph = [[0] * 100 for _ in range(100)]

for i in range(N):
    x, y, nx, ny = map(int, input().split())
    for i in range(x, nx+1):
        for j in range(y, ny+1):
            graph[i-1][j-1] += 1
cnt= 0
for i in range(100):
    for j in range(100):
        if graph[i][j] > M:
            cnt += 1

print(cnt)
