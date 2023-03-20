import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
R, C, T = map(int, input().split())

def clean_top(x, y):
    for i in range(x-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    
    for j in range(C-1):
        graph[0][j] = graph[0][j+1]
    
    for k in range(x):
        graph[k][C-1] = graph[k+1][C-1]

    for l in range(C-1, 1, -1):
        graph[x][l] = graph[x][l-1]

    graph[x][1] = 0

def clean_bottom(x, y):
    for i in range(x+1, R-1):
        graph[i][0] = graph[i+1][0]
    
    for j in range(C-1):
        graph[R-1][j] = graph[R-1][j+1]
    
    for k in range(R-1, x, -1):
        graph[k][C-1] = graph[k-1][C-1]

    for l in range(C-1, 1, -1):
        graph[x][l] = graph[x][l-1]

    graph[x][1] = 0

def chk():
    arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            x, y = i, j
            count = 0
            if graph[i][j] == 0:
                continue
            if graph[i][j] == -1:
                arr[i][j] = -1
                continue         
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                    count += 1
                    arr[nx][ny] += graph[x][y] // 5
            arr[x][y] += (graph[x][y] - (graph[x][y] // 5) * count)

    for i in range(R):
        for j in range(C):
            graph[i][j] = arr[i][j]

    for i in range(R):
        for j in range(C):
            graph[i][j] = arr[i][j]

graph = []
clean = []
for i in range(R):
    graph.append(list(map(int, input().split())))

for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            clean.append((i, j))


for i in range(T):
    chk()
    clean_top(clean[0][0], clean[0][1])
    clean_bottom(clean[1][0], clean[1][1])

res = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            res += graph[i][j]

print(res)
