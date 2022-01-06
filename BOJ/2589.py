from collections import deque

def bfs(x, y):
    distance = 0
    queue = deque()
    queue.append([x, y, 0]) #  시작 노드를 큐에 넣어둠
    visited[x][y] = 1

    while queue:
        x,y,d = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= a or ny >= b:
                continue
            if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                queue.append((nx, ny, d+1))
                visited[nx][ny] = 1
                distance = d + 1
    return distance


dx = [0,0,-1,1]
dy = [-1,1,0,0]

a, b = map(int, input().split())

graph = [input() for _ in range(a)]
visited = [[0] * b for _ in range(a)]
max_distance = 0

for i in range(a):
    for j in range(b):
        if graph[i][j] == 'L':
            visited = [[0] * b for _ in range(a)]
            max_distance = max(max_distance, bfs(i, j))

print(max_distance)

# BFS 설명

# 큐에 값이 존재하지 않을때까지 반복
# 맨 앞에 큐 꺼내서 가져오기
# 상하좌우 & 방문 비교
# 방문 안했으면 큐에 추가, 방문했다고 표시, 거리 1씩 증가
 

# Main

# 그래프의 모든 원소 탐색
# 탐색할때마다 매번 방문리스트 초기화
# 탐색끝나면 max_distance랑 비교해서 큰 값 넣어주기