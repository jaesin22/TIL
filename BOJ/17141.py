import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

res = float("inf")

def bfs(v): # v는 combination 한줄씩 입력받음
    queue = deque(v)
    visited = [[-1] * N for _ in range(N)]
    m = 0 # 최소 횟수를 찾기 위한 변수    
    for x, y in queue:
        visited[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[a][b] + 1
                    m = max(m, visited[a][b] + 1)
                    

    # bfs가 끝난 이후 바이러스에 감염되지 않은 빈 칸이 있다면 감염시킬수 없는 경우
    # 따라서 inf를 리턴해줌
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and graph[i][j] != 1:
                return res

    return m



N, M = map(int, input().split())

graph = []
virus = []
for x in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))

# 바이러스의 좌표들 중 M개를 뽑은 모든 경우에 대해서 bfs 수행하며 최솟값 갱신
for v in combinations(virus, M):
    res = min(bfs(v), res)

# 탐색하지 못하는 경우 answer에는 inf값이 들어있다
if res == float("inf"):
    print(-1)
else : 
    print(res)
