import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    global cnt
    while snake:
        cnt += 1
        a, b = snake.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                snakeArray[nx][ny] == 1
                if graph[nx][ny] == 2:
                    graph[nx][ny] == 0
                elif graph[nx][ny] == 0:
                    snakeArray[a][b] = 0
                graph[a][b] = 1
                snake.append((nx, ny))
        
cnt = 1
snake = deque()
N = int(input())
K = int(input())
snake.append((0, 1))
snakeArray = [[0] * N for _ in range(N)]
apple = deque()
graph = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[b][a] = 2

L = int(input())
dir_snake = deque()
for x in range(L):
    X, C = map(str, input().split())
    dir_snake.append((int(X), C))