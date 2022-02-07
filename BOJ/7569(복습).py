from collections import deque
import sys
input = sys.stdin.readline
m,n,h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)]]
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

queue = deque()
