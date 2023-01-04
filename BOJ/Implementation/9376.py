import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
T = int(input())


def BFS(x, y):
    queue = deque()
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    queue.append([x, y])
    visited[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if visited[nx][ny] == -1:
                    if prison[nx][ny] == '.':
                        queue.appendleft([nx, ny])
                        visited[nx][ny] = visited[a][b]
                    elif prison[nx][ny] == '#':
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[a][b] + 1

    return visited


for _ in range(T):
    h, w = map(int, input().split())
    prison = [['.'] * (w + 2)]
    for i in range(h):
        prison.append(list('.' + input().strip() + '.'))
    prison.append(['.'] * (w + 2))
    start = []

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if prison[i][j] == '$':
                start.append([i, j])
                prison[i][j] = '.'

    cnt1 = BFS(start[0][0], start[0][1])
    cnt2 = BFS(start[1][0], start[1][1])
    cnt3 = BFS(0, 0)

    ans = float('inf')
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if cnt1[i][j] != -1 and cnt2[i][j] != -1 and cnt3[i][j] != -1:
                if prison[i][j] == '.':
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j])
                elif prison[i][j] == '#':
                    ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j] - 2)
    print(ans)