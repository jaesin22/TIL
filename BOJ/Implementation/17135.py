import sys
input = sys.stdin.readline
from collections import deque

#좌 상 우 순서, 아래는 볼 필요 없음
dx = [0,-1,0]
dy = [-1,0,1]

def down():
    for j in range(M):
        for i in range(N-2,-1,-1):
            graph[i+1][j] = graph[i][j]
    for i in range(M):
        graph[0][i] = 0


N, M, D = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

down()

down()

for i in graph:
    print(i)