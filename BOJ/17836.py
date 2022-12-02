import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
visited = [[0] * M  for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    gonju = 10000000
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 1

    while q:
        a, b, time = q.popleft()
        if a == N-1 and b == M-1:
            gonju = min(gonju, time)
            print(gonju)
            return

        if time >= T:
            print("Fail")
            return

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]==0:
                if graph[nx][ny] == 1:
                    continue
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, time+1))
                else:
                    visited[nx][ny] = 1
                    diff = time + 1 + abs(nx-(N-1)) + abs(ny-(M-1)) # queue를 다 돌면서 공주가 있는 위치에 오면 현재 걸린 시간과 최소 시간을 최솟값 비교를 통해 갱신
                    if diff <= T:
                        gonju = diff

bfs()