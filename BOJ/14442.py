import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph =[]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    queue = deque()
    queue.append((0, 0, K, 1))

    while queue:
        a, b, k, d = queue.popleft()
        if a == N-1 and b == M-1:
            print(d)
            return
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if k > 0:
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 1 and visited[nx][ny][k-1] == 0:
                        visited[nx][ny][k-1] = visited[a][b][k-1] + 1 
                        queue.append((nx, ny, k-1, d + 1))

        for j in range(4):
            nx = a + dx[j]
            ny = b + dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = visited[a][b][k] + 1
                    queue.append((nx, ny, k, d + 1))
    print(-1)
    return 

bfs()