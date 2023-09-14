import sys
from collections import deque
input = sys.stdin.readline
# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 로봇 청소기 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

N, M = map(int, input().split())
r, c, direction = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
cnt = 1
clean_cnt = 0
while True:
    turn_left()

    nx = r + dx[direction]
    ny = c + dy[direction]
    if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 0 and visited[nx][ny] == 0:
            cnt += 1
            visited[nx][ny] = 1
            r, c = nx, ny
            clean_cnt = 0
            continue

        else:
            clean_cnt += 1
        
    if clean_cnt == 4:
        nx = r - dx[direction]
        ny = c - dy[direction]
        if graph[nx][ny] == 0:
            r, c = nx, ny
        else:
            break

        clean_cnt = 0

print(cnt)