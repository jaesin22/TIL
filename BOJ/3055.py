import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

def bfs():
    while water:
        a, b = water.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.' and visited_water[nx][ny] == 0:
                    visited_water[nx][ny] = visited_water[a][b] + 1
                    water.append((nx, ny))
        
    while dochi:
        a, b, c = dochi.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if visited_water[nx][ny] == 0 or visited_water[nx][ny] > visited_dochi[a][b] + 1:
                    if graph[nx][ny] == 'D':
                        print(c)
                        return
                    if graph[nx][ny] == '.' and visited_dochi[nx][ny] == 0:
                        visited_dochi[nx][ny] = visited_dochi[a][b] + 1
                        dochi.append((nx, ny, c+1))
    
    print("KAKTUS")
    return


dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph = []
for x in range(R):
    graph.append(list(map(str, input().rstrip())))

water = deque()
dochi = deque()
visited_water = [[0] * C for _ in range(R)]
visited_dochi = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            dochi.append((i, j, 1))
        if graph[i][j] == '*':
            water.append((i, j))
        
bfs()