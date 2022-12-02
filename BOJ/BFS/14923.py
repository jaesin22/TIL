import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
visited = [[[0] * 2 for _ in range(M)]for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]


graph = []
for _ in range(N):
    graph.append(list(map(int ,input().split())))



def bfs():
    queue = deque()
    queue.append((Hx-1, Hy-1, 0, 0))
    # visited[Hx-1][Hy-1][0] = 1

    while queue:
        a, b, wall, c = queue.popleft()

        if (a, b) == (Ex-1, Ey-1):
            print(visited[a][b][wall])
            return
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][wall] == 0:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny, wall, c + 1))
                    visited[nx][ny][wall] = visited[a][b][wall] + 1
                
                if wall == 0 and graph[nx][ny] == 1:
                    queue.append((nx, ny, 1, c + 1))
                    visited[nx][ny][1] = visited[a][b][wall] + 1
    print(-1)
    return

bfs()