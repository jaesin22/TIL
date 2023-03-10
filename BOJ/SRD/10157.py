from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


C, R = map(int, input().split())
N = int(input())
graph = [[0 for _ in range(R)] for _ in range(C)]

def search():  
    dir = 0
    queue = []
    queue.append([0, 0])
    graph[0][0] = 1
    while queue:
        a, b = queue.pop()
        if graph[a][b] == N:
            print(a + 1, b + 1)
            return
        nx = a + dx[dir]
        ny = b + dy[dir]
        if 0 <= nx < C and 0 <= ny < R and not graph[nx][ny]:
            graph[nx][ny] = graph[a][b] + 1
            queue.append([nx,ny])
            continue
        else:
            dir = (dir + 1) % 4
            nx = a + dx[dir]
            ny = b + dy[dir]
            if 0 <= nx < C and 0 <= ny < R and not graph[nx][ny]:
                graph[nx][ny] = graph[a][b] + 1
                queue.append([nx,ny])
                continue
    print(0)
    return

search()