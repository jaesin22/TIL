import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int,input().split())
m = []
for _ in range(R):
    m.append(list(input().rstrip()))
answer = [0, 0]         # sheep, wolf
q = deque()
visited = [[False] * C for _ in range(R)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
 
def bfs(i, j):
    sheep, wolf = 0, 0
    if m[i][j] == 'v':
        wolf = 1
    if m[i][j] == 'k':
        sheep = 1
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and m[nx][ny] != '#':
                visited[nx][ny] = True
                if m[nx][ny] == 'v':
                    wolf += 1
                elif m[nx][ny] == 'k':
                    sheep += 1
                q.append((nx, ny))
    
    if sheep > wolf:
        answer[0] += sheep
    else:
        answer[1] += wolf
 
 
for i in range(R):
    for j in range(C):
        if m[i][j] != '#' and not visited[i][j]:
            bfs(i, j)
 
print(*answer)