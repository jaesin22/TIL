import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
graph = []
queue = deque()
visited = [[0] * M for _ in range(N)]
for x in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            queue.append((i, j))
            visited[i][j] = 1

print(queue)

def bfs():
    cnt = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:               
                    visited[nx][ny] = visited[a][b] + 1
                    graph[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))  
            else: 
                print(cnt)
                return

    print(-1)
    return


bfs()
