import sys
input = sys.stdin.readline
from collections import deque


# 물고기를 먹으러갈 때마다 bfs로 이동한다.
# bfs로 이동하고 이동한 칸 수 만큼 answer에 더해준다. 
# 현재 상어의 크기 만큼 물고기를 먹었으면 상어의 크기 + 1해준다. 
# 틀렸던 부분 ) "먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기 -> 가장 위에 -> 가장 왼쪽에"  
# : 이 부분 구현은 bfs와 move의 순서 조정으로 할 수 있을 줄 알았는데, 먹을 수 있는 물고기를 다 고려해준 후에 sort를 해줘야지 정확한 답이 나온다.

N = int(input())
graph = []
visited = [[0] * N for _ in range(N)]
# 북, 남, 동, 서
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(N):
    graph.append(list(map(int, input().split())))

sx, sy = 0,0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            sx, sy = i, j
            graph[i][j] = 0

def bfs(x, y, shark):
    queue = deque()
    queue.append((x, y, 0))
    visited = [[0] * N for _ in range(N)]
    eat = []
    while queue:
        a, b, c = queue.popleft()
        if visited[a][b] != 0:
            continue
        visited[a][b] = c
        if graph[a][b] < shark and graph[a][b] != 0:
            eat.append((c, a, b))
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] <= shark:
                    queue.append((nx, ny, c + 1))
        if not eat:
            return (-1, -1, -1)
        eat.sort()
        graph[eat[0][1]][eat[0][2]] = 0
        return eat[0]

shark = 2
answer = 0

isContinue = True
while isContinue:
    for i in range(shark):
        c, x, y = bfs(sx, sy, shark)
        # print(c)
        if c == -1:
            isContinue = False
            break
        sx, sy = x, y
        answer += c
    else:
        shark += 1

print(answer)