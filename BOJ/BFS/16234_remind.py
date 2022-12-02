import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    connet = deque()
    visited[x][y] = 1
    count, people = 0, 0

    while queue:
        a, b = queue.popleft()
        connet.append((a, b))
        people += graph[a][b]
        count += 1

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    diff = abs(graph[a][b] - graph[nx][ny])
                    if L <= diff <= R:
                        visited[nx][ny] = count
                        queue.append((nx, ny))
        
    while connet:
        a, b = connet.popleft()
        graph[a][b] = people // count
    
    if count == 1:
        return 0
    return 1


answer = 0
while True:
    break_cnt = 0
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue.append((i, j))
                break_cnt += bfs(i, j)
    
    if break_cnt == 0:
        break
    else:
        answer += 1

print(answer)