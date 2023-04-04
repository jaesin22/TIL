import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def search():
    res = 0
    for _ in range(k):
        while queue:
            a, b = queue.popleft()
            smell_cnt = 0
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                

    

N, M, k = map(int, input().split())
queue = deque()
graph = []
smell = [[0] * N for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            queue.append((i, j))
            smell.append((i, j, k))


first_dir = [list(map(int, input().split()))]
shark_dir = []
for i in range(4):
    arr = []
    for j in range(4):
        a, b, c, d = map(int, input().split())
        arr.append([a, b, c, d])
    shark_dir.append(arr)

