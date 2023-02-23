import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
def bfs():
    queue = deque()
    queue.append((0, 0, 0, 1))
    visited[0][0][0] = 1

    while queue:
        a, b, c, d = queue.popleft()

        if N-1 == a and M-1 == b:
            return d
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and c < K and visited[nx][ny][c+1] == 0:
                    if d & 1:
                        visited[nx][ny][c+1] = 1
                        queue.append((nx, ny, c + 1, d + 1))
                    else:
                        queue.append((a, b, c, d + 1))

                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = 1
                    queue.append((nx, ny, c, d + 1))

    return -1


print(bfs())