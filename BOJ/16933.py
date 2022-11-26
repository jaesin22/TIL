import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
def bfs():
    queue = deque()
    queue.append((0, 0, K, 1))
    day = True
    visited[0][0][K] = 1

    while queue:
        a, b, k, d = queue.popleft()

        if N-1 == a and M-1 == b:
            print(d)
            return
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if k > 0:
                    if day == True and graph[nx][ny] == 1:
                        if graph[nx][ny] == 1 and visited[nx][ny][k-1] == 0:
                            visited[nx][ny][k-1] = visited[a][b][k-1] + 1
                            if day == True: day = False
                            else : day = True
                            queue.append((nx, ny, k-1, d + 1))

                    if day == False and graph[nx][ny] == 1:
                        visited[nx][ny][k] = visited[a][b][k] + 1
                        queue.append((a, b, k, d + 1))             
                        if day == True: day = False
                        else : day = True
                
                if graph[nx][ny] == 0 and visited[nx][ny][k] == 0:
                        visited[nx][ny][k] = visited[a][b][k] + 1
                        if day == True: day = False
                        else : day = True
                        queue.append((nx, ny, k, d + 1))
    
    print(-1)
    return


bfs()