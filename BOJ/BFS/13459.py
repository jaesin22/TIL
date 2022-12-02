from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
N, M = map(int, input().split())
graph = []
for x in range(N):
    graph.append(list(map(str, input().rstrip())))

rx, ry, bx, by = 0,0,0,0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

queue = deque()

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    count = 0
    while queue:
        for _ in range(len(queue)):
            rx, ry ,bx ,by = queue.popleft()
            if count > 10:
                print(0)
                return 

            if graph[rx][ry] == 'O':
                print(1)
                return

            for i in range(4):
                nrx, nry = rx, ry # 어차피 while문으로 계속 위치 값 이동할 테니까 최초에 두번 이동하지 않을 수 있도록 nrx, nry를 rx + dx[i], ry + dy[i]로 하지 않음

                while True: # #일때까지 혹은 구멍일 때 까지 움직임
                    nrx += dx[i]
                    nry += dy[i]
                    
                    if graph[nrx][nry] == '#': #벽이였던 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break

                    if graph[nrx][nry] == 'O':  # 도착했을 때
                        break
                
                nbx, nby = bx, by # 어차피 while문으로 계속 위치 값 이동할 테니까 최초에 두번 이동하지 않을 수 있도록 nbx, nby를 bx + dx[i], by + dy[i]로 안함 

                while True:
                    nbx += dx[i]
                    nby += dy[i]

                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    
                    if graph[nbx][nby] == 'O':
                        break
                
                if graph[nbx][nby] == 'O': # 파란 구슬이 마저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx-rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else :
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited: # 방문해본 적이 없는 위치라면 새로 큐에 추가 후 방문처리
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(0)

bfs(rx, ry, bx, by)