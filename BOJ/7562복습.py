import sys
from collections import deque
input = sys.stdin.readline


dx = [-2, -2, 2,2, -1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

def bfs(start_x,start_y, end_x, end_y):
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = 1

    while queue:
        a, b, c = queue.popleft()
        if a == end_x and b == end_y:
            print(c)
            return
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
                queue.append((nx, ny, c + 1))
                visited[nx][ny] = 1
                



T = int(input())
for x in range(T):
    I = int(input())
    visited = [[0] * I for _ in range(I)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    if start_x == end_x and start_y == end_y:
        print(0)
        continue

    bfs(start_x, start_y, end_x, end_y)