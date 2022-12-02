import sys
from collections import deque
input = sys.stdin.readline

# 문제 해결 아이디어
# 1. 시작지점(0, 0)에서 bfs를 한다. (visited = 검은 방을 흰 방으로 바꾼 횟수)

#     - 해당 위치가 흰 방(1)이면 이전 visited의 값으로 초기화, appendleft(흰 방 먼저 탐색)

#     - 해당 위치가 검은 방(0)이면 이전 visited에서 1을 더해서 초기화, append

# 2. x, y 가 도착지점(N-1, N-1)이면 return visited[x][y]

 

# 흰 방을 먼저 탐색하기 때문에

# 처음 도착지점에 도착한 visited의 값은 최솟값이 된다.

# visited값을 출력할 땐 visited의 초기화를 -1로 하자 !



N = int(input())

visited = [[-1] * N for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = 0

    while queue:
        a, b, c = queue.popleft()

        if (a, b) == (N-1, N-1):
            print(visited[N-1][N-1])
            return

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[a][b]                  
                    queue.appendleft((nx, ny, c))

                elif graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[a][b] + 1
                    queue.append((nx, ny, c+1))


bfs()

