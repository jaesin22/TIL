import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for x in range(N):
    graph.append(list(map(str, input().rstrip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
rx, ry, bx, by = 0,0,0,0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j

def bfs(rx, ry, bx, by):
    queue = deque()
    visited = []
    queue.append((rx, ry, bx, by))
    visited.append((rx, ry, bx, by))
    count = 0
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()

            if count > 10:
                print(-1)
                return
                
            if graph[rx][ry] == 'O':
                print(count)
                return
            
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break                    
                    if graph[nrx][nry] == 'O':
                        break
                
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    
                    if graph[nbx][nby] == 'O':
                        break
                        
                if graph[nbx][nby] == 'O': # 파란 구슬이 도착하면 실패이기 때문에 해당 경우 무시
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동 왜냐면 그래야 도착을 더 빨리 이동한 구슬이 할테니까
                        nrx -= dx[i]
                        nry -= dy[i]
                    else :
                        nbx -= dx[i]
                        nby -= dy[i]
            
                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    queue.append((nrx, nry, nbx, nby))
                        
        count += 1
    print(-1)
bfs(rx, ry, bx, by)