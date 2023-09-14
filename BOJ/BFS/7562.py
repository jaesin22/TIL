import sys
from collections import deque
input = sys.stdin.readline
dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]


def bfs(queue, x, y, visited, graph):
    while queue:

        a, b, c = queue.popleft()
        if a == x and b == y:
            return c
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, c + 1))


T = int(input())
for i in range(T):
    I = int(input())
    visited = [[0] * I for _ in range(I)]
    graph = [[0] * I for _ in range(I)]
    queue = deque()
    x, y = 0, 0
    for j in range(2):
        a, b = map(int, input().split())
        if j == 0:
            queue.append((a, b, 0))
        if j == 1:
            x, y = a, b

    print(bfs(queue, x, y, visited, graph))
