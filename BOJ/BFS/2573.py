from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
day = 0
check = False

def bfs(x,y):
    queue.append((x,y))
    while queue:
        a,b = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[a][b] += 1
    return 1

# 빙산이 분리될때까지 돌아줌
while True:
    visited = [[0] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == 0:
                result.append(bfs(i,j))
    
    print(result)

    # 빙산을 깍아줌           
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    if len(result) == 0: # 빙산이 다없어질때까지 분리가 되지않으면 break
        break
    if len(result) >= 2: # 빙산이 분리되면 break
        check = True
        break
    day += 1

if check:        
    print(day)
else:
    print(0)


# 빙산은 근처에 물에 개수에 영향을 받아 빙산이 깍인다. 그래서 bfs를 돌때 elif에 주변이 0일 경우 count 리스트에 +1을 해줘서 저장해준다.

# graph에 바로 반영을 하게 되면 주변 빙산에 영향이 있기 때문에 따로 저장해뒀다가 한번에 빙산을 깍아줘야한다.

# bfs가 한번만 실행된다면 섬이 아직 분리가 되지 않았고 2번이상 실행된다면 분리가 되었다는 것이다.

# bfs 리턴값을 result에 append시켜 result 길이 bfs 실행 횟수를 알 수 있다.

# while문으로 섬이 분리될때 까지 돌아준다.