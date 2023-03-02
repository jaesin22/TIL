import sys
from collections import deque
input = sys.stdin.readline

N, M, D = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[[0] * M for _ in range(N)] for i in range(D)]
