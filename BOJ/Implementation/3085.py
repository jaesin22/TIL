import sys
import copy
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def check(x, y, color):
    res = 0
    for i in range(N):
        if graph[i][0] == color:
            res += 1
    cnt = 0
    for j in range(N):
        if graph[0][j] == color:
            cnt += 1
    res = max(res, cnt)

    return res



def search(x, y):
    global res
    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[a][b] != graph[nx][ny]:
                    copyGraph = copy.deepcopy(graph)
                    temp = copyGraph[nx][ny]
                    copyGraph[nx][ny] = copyGraph[a][b]
                    copyGraph[a][b] = temp

N = int(input())
res = 0
graph = [list(map(str, input().rstrip())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        search(i, j)