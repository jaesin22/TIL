from collections import deque
import sys

# 가로 세로 길이
R, C = map(int, sys.stdin.readline().split())

graph = deque()
# 방문체크
visited = [[0] * C for _ in range(R)]

# 입력
for _ in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x, y):
    global w, s
    visited[x][y] = 1
    # 늑대면 a 1 증가
    if graph[x][y] == 'v':
        w += 1
    elif graph[x][y] == 'k':
        s += 1
    
    # 4방 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있고, #이 아니고 방문을 하지 않았으면 dfs 돌자
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and visited[nx][ny] == 0:
            DFS(nx, ny)
    

wolf = 0 # 총 양 마리 수
sheep = 0 # 총 늑대의 마리 수

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visited[i][j] == 0:
            w = 0
            s = 0
            DFS(i, j)
            if w >= s :
                s = 0
            else :
                w = 0
                
            wolf += w
            sheep += s

print(sheep, wolf)