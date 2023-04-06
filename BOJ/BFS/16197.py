import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(ax, ay, bx, by):
    check = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    check[ax][ay][bx][by] = 0
    queue = deque()
    queue.append([ax, ay, bx, by])

    while queue:
        rx, ry, bx, by = queue.popleft()
        if check[rx][ry][bx][by] >= 10:
            break

        for i in range(4):
            nrx = rx + dx[i]
            nry = ry + dy[i]
            nbx = bx + dx[i]
            nby = by + dy[i]

            if not (0 <= nrx < N and 0 <= nry < M) and not (0 <= nbx < N and 0 <= nby < M):
                continue

            if not (0 <= nrx < N and 0 <= nry < M):
                return check[rx][ry][bx][by] + 1
            if not (0 <= nbx < N and 0 <= nby < M):
                return check[rx][ry][bx][by] + 1
            
            if graph[nrx][nry] == '#':
                nrx -= dx[i]
                nry -= dy[i]
            
            if graph[nbx][nby] == '#':
                nbx -= dx[i]
                nby -= dy[i]
            
            #check 배열의 이동할 위치에 현 횟수 + 1한 횟수 표시, 이동할 위치 큐 담기
            if check[nrx][nry][nbx][nby] == -1:
                check[nrx][nry][nbx][nby] = check[rx][ry][bx][by] + 1
                queue.append((nrx, nry, nbx, nby))

    return -1

N, M = map(int, input().split())
graph = []
rx, ry, bx, by = 0, 0, 0, 0
flag = False
for i in range(N):
    graph.append(list(input().rstrip()))
    for j in range(M):
        if graph[i][j] == 'o':
            if not flag:
                rx, ry = i, j
                flag = True
            else:
                bx, by = i, j

print(bfs(rx, ry, bx, by))