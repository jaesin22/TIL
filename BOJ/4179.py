import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fbfs():
    while fq:
        a, b = fq.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != "#" and visited_f[nx][ny] == 0:
                    visited_f[nx][ny] = visited_f[a][b] + 1
                    fq.append((nx, ny))

def hbfs():
    while hq:
        a, b = hq.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != '#' and visited_j[nx][ny] == 0:
                    if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_j[a][b] + 1:
                        visited_j[nx][ny] = visited_j[a][b] + 1
                        hq.append((nx, ny))

            else:
                print(visited_j[a][b])
                return

    print("IMPOSSIBLE")
    return

R, C = map(int, input().split())
graph = []
hq = deque()
fq = deque()
visited_j = [[0] * C for _ in range(R)]
visited_f = [[0] * C for _ in range(R)]
for i in range(R):
    graph.append(list(input().strip()))
    for j in range(C):
        if graph[i][j] == "J":
            hq.append((i, j))
            visited_j[i][j] = 1
        elif graph[i][j] == "F":
            fq.append((i, j))
            visited_f[i][j] = 1
fbfs()
hbfs()