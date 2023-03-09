import sys
input = sys.stdin.readline
# 왼 오 위 아래
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
N = int(input())
graph = []
for i in range(N):
    graph.append(input().strip())

res = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] != '.':
            s = int(graph[i][j])
            x, y = i, j
            res[i][j] = '*'
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if res[nx][ny] != '*' and res[nx][ny] != 'M':
                        res[nx][ny] += s
                        if res[nx][ny] >= 10:
                            res[nx][ny] = 'M'

for i in range(N):
    for j in range(N):
        print(res[i][j], end='')
    print()