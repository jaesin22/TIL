import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int ,input().split())))

visited = [0] * M