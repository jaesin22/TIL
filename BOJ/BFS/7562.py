from  collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[0] * I for _ in range(I)]
    visited[start_x][start_y] = 1

    dx = [-2, -2, 2,2, -1,1,-1,1]
    dy = [-1,1,-1,1,-2,-2,2,2]

    queue = deque()
    queue.append((start_x, start_y, 0))

    while queue:
        x, y, c = queue.popleft()
        if x == end_x and y == end_y:
            print(c)
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, (c + 1)))