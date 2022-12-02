from sys import stdin
input = stdin.readline
from collections import deque

dz = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dx = (0, 0, 0, 0, -1, 1)

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 밖이거나
            if not (0 <= nz < L and 0 <= ny < R and 0 <= nx < C):
                continue
            # 이미 방문했거나 벽이면
            if visited[nz][ny][nx] or graph[nz][ny][nx] == "#":
                continue
            # 도착지면 출력 후 리턴
            if graph[nz][ny][nx] == "E":
                print("Escaped in {} minute(s).".format(visited[z][y][x]))
                return
            # 가능한 다음 위치에 거리 표시하고 큐에 담기
            visited[nz][ny][nx] = visited[z][y][x] + 1
            queue.append((nz, ny, nx))
    
    print("Trapped!")   # 불가능한 경우
    return

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    graph = []      # 빌딩 3차원 배열로 표현
    sl, sr, sc = -1, -1, -1     # 시작 좌표
    queue = deque()
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        graph.append([list(input().rstrip()) for _ in range(R)])
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == "S":
                    queue.append((i, j, k))
                    visited[i][j][k] = 1
        input()
    bfs()