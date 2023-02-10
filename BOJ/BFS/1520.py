from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))


def bfs():
    queue = deque()
    visited = [[0] * N for _ in range(M)]
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        a, b = queue.popleft()
        if a == M-1 and b == N-1:
            return 1

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] < graph[a][b] and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    return 0

    

cnt = 0
for i in range(M):
    for j in range(N):
        res = bfs()
        cnt += res

print(cnt)     



