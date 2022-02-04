from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = (1, 0, 0, -1, 0, 0)
dy = (0, 1, 0, 0, -1, 0)
dz = (0, 0, 1, 0, 0, -1)
q = deque()

def print_max():
    _max = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if not board[i][j][k]:
                    return False
                if _max < board[i][j][k]:
                    _max = board[i][j][k]
    return _max-1

def solve_bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if not board[nx][ny][nz]:
                    board[nx][ny][nz] = board[x][y][z] + 1
                    q.append((nx, ny, nz))
zero = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                q.append((i, j, k))
            elif not board[i][j][k]:
                zero = True
if not zero:
    print(0)
else:
    solve_bfs()
    out = print_max()
    if not out:
        print(-1)
    else:
        print(out)