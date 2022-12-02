import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int ,input().rstrip()))for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

ans = 0

def bfs():
    queue = deque()
    visited[0][0][0] = 1
    queue.append((0,0,0))
    
    while queue:
        a, b, wall = queue.popleft()
        if (a, b) == (N-1, M-1):
            print(visited[a][b][wall])
            return

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][wall] == 0:
                #벽이 아니라면 이동하고, 이전 경로 + 1 visited배열에 저장
                if graph[nx][ny] == 0:
                    queue.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[a][b][wall] + 1

                # 벽 1번도 안 부쉈고 다음 이동할 곳이 벼깅라면
                if wall == 0 and graph[nx][ny] == 1:
                    # 벽을 부순 상태를 1로 표현
                    queue.append((nx, ny, 1))
                    #벽 부순 상태의 visited[nx][ny][1]에 이전 경로 + 1 저장
                    visited[nx][ny][1] = visited[a][b][wall] + 1
    
    print(-1)
    return

bfs()