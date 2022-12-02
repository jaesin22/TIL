import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
R, C = map(int ,input().split())
graph = []
visited = [[0] * C for _ in range(R)]
water_visited = [[0] * C for _ in range(R)]
time = 0
bird = deque()
water = deque()
for i in range(R):
    graph.append(list(map(int, input().rstrip())))
    for j in range(C):
        if graph[i][j] == 'L':
            bird.append((i, j))
        if graph[i][j] == '.':
            water.append((i, j))
            water_visited[i][j] = 1

bird.pop()

def iceToWater():
    global time
    while water:
        a, b = water.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[a][b] == '.' and water_visited[nx][ny] == 0:
                    if graph[nx][ny] == '#' and water_visited[nx][ny] == 0:
                        graph[nx][ny] = '.'
                        water_visited[nx][ny] = 1
        time += 1

def bfs():
    while bird:
        a, b = bird.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
