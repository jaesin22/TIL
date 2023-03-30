import sys, copy
from collections import deque
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def curve(x, y, dir, generation):
    queue = deque()
    visited[x][y] = True
    nx, ny = x + dx[dir], y + dy[dir]
    visited[nx][ny] = True
    queue.append(dir)
    for i in range(1, generation+1):
        queue_copy = copy.deepcopy(queue)
        while queue_copy:
            direction = queue_copy.pop()
            direction = (direction + 1) % 4
            nx += dx[direction]
            ny += dy[direction]
            visited[nx][ny] = True
            queue.append(direction)

N = int(input())
visited = [[False] * (101) for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve(y, x, d, g)

res = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
            res += 1

print(res)