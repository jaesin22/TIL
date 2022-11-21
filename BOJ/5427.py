import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    while fq:
        a, b = fq.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == '.' and visited_f[nx][ny] == 0:
                    visited_f[nx][ny] = visited_f[a][b] + 1
                    fq.append((nx, ny))
    while hq:
        a, b, c = hq.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if not(0 <= nx < h and 0 <= ny < w): #탈출 했을 때
                return c
            if 0 <= nx < h and 0 <= ny < w:
                if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_h[a][b] + 1:
                    if graph[nx][ny] == '.' and visited_h[nx][ny]== 0:
                        visited_h[nx][ny] = visited_h[a][b] + 1
                        hq.append((nx, ny, c+1))
    return "IMPOSSIBLE"


T = int(input())
for _ in range(T):
    graph = []
    hq = deque()
    fq = deque()
    w, h = map(int, input().split())
    visited_f = [[0] * w for _ in range(h)]
    visited_h = [[0] * w for _ in range(h)]
    for x in range(h):
        graph.append(list(map(str, input().rstrip())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                visited_h[i][j] = 1
                hq.append((i, j, 1))
            elif graph[i][j] == '*':
                visited_f[i][j] = 1
                fq.append((i, j))
    print(bfs())