from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, Q = map(int, input().split())
graph = []
for _ in range(2 ** N):
    graph.append(list(map(int, input().split())))

