import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]

# 1. 3차원 count 리스트를 정의한다 (count[x][y][남은 말처럼 이동가능한 횟수])

# 2. q가 빌 때 까지

#   - 말처럼 이동 가능한 횟수(K)가 0보다 크면 말처럼 이동

#      - 해당위치가 장애물이 아니고, 해당 방법으로 이동한 적이 없으면(count[nx][ny][K]==0)

#      - K-1한 위치에 이전 count +1

#   - 원숭이처럼 이동

#   - 목표위치에 도착하면 return

# 3. 출력

def bfs():
    queue = deque()
    queue.append((0, 0, K))

    while queue:
        x, y, k = queue.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][k]
        
        if k > 0:
            for i in range(8):
                nx = x + horse_dx[i]
                ny = y + horse_dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if graph[nx][ny] == 0 and visited[nx][ny][k-1] == 0:
                        visited[nx][ny][k-1] = visited[x][y][k] + 1
                        queue.append((nx, ny, k-1))
                
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
    return -1


K = int(input())
W, H = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))

visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]

print(bfs())

