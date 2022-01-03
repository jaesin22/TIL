import sys
from collections import deque

N = int(sys.stdin.readline())
s = []

max_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx,ny])



for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    s.append(a)

for i in range(0, 101):
    visited = [[0] * N for i in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if s[j][k] <= i:
                visited[j][k] = 1
    for j in range(N):
        for k in range(N):
            if visited[j][k] == 0:
                visited[j][k] = 1
                bfs(j, k)
                cnt += 1
    if cnt == 0:
        break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)