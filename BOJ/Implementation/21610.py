import sys
from collections import deque
input = sys.stdin.readline
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def makecloud(queue):
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (i, j) not in queue:
                graph[i][j] -= 2
                cloud.append((i, j))


def move(x, y):
    queue = []
    A = [1,3,5,7]
    while cloud:
        a, b = cloud.popleft()
        for i in range(y):
            a = a + dx[x]
            b = b + dy[x]
            
            if a >= N:
                a = 0
            elif a <= -1:
                a = N-1

            if b >= N:
                b = 0
            elif b <= -1:
                b = N-1
        queue.append((a, b))

    watercopy(queue)
    makecloud(queue)


def watercopy(queue):
    for i, j in queue:
        graph[i][j] += 1
    
    for k, l in queue:
        cnt = 0
        for z in range(1, 8, 2):
            nx = k + dx[z]
            ny = l + dy[z]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > 0:
                    cnt += 1
            
        graph[k][l] += cnt

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
arr = []
for _ in range(M):
    a, b = map(int, input().split())
    arr.append((a, b))


cloud = deque()
cloud.append((N-1, 0))
cloud.append((N-1, 1))
cloud.append((N-2, 0))
cloud.append((N-2, 1))

for i, j in arr:
    move(i-1, j)

res = 0
for k in range(N):
    for l in range(N):
        res += graph[k][l]

print(res)
    