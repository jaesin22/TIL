import sys
from collections import deque

R, C = map(int, input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def fbfs():
    while fq:
        a, b = fq.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < R and 0 <=ny < C:
                if graph[nx][ny] != '#' and visited_f[nx][ny] == 0:
                    fq.append((nx, ny))
                    visited_f[nx][ny] = visited_f[a][b] + 1


def hbfs():
    while hq:
        a, b = hq.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != '#' and visited_j[nx][ny] == 0:
                    if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_j[a][b] +1: #불이 이미 퍼지지 않은 곳이거나 혹은 불이 도달하는 시간보다 더 짧은 시간안에 지훈이 도달할 수 있다면 해당 위치에 대한 값을 기록해주면 된다.                 
                        visited_j[nx][ny] = visited_j[a][b] + 1
                        hq.append((nx, ny))

            else:
                # 만약 nx와 ny가 범위를 벗어나게 된다면 지훈이 무사히 탈출한 것으로 간주할 수 있으므로 x와 y까지의 이동거리를 리턴해주면 답을 구할 수 있다.
                print(visited_j[a][b])
                return
    print("IMPOSSIBLE")
    return
graph = []
visited_j = [[0] * C for _ in range(R)]
visited_f = [[0] * C for _ in range(R)]
hq = deque()
fq = deque()
for i in range(R):
    graph.append(list(input().rstrip()))

    for j in range(C):
        if graph[i][j] == 'F':
            fq.append((i, j))
            visited_f[i][j] = 1
        if graph[i][j] == 'J':
            hq.append((i, j))
            visited_j[i][j] = 1
        
fbfs()    
hbfs()
