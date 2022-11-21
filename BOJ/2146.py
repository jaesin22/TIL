import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]
graph = []
visited = [[0] * N for _ in range(N)]

for x in range(N):
    graph.append(list(map(int, input().split())))

