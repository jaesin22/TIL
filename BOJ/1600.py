import sys
from collections import deque
input = sys.stdin.readline

# da = [-2,-1, 1, 2, 2, 1, -1, -2]
# db = [-1, -2, -2, -1, 1, 2, 2, 1]
da = [-2, -2, 2,2, -1,1,-1,1]
db = [-1,1,-1,1,-2,-2,2,2]

dx = [0,0,-1,1]
dy = [-1.1,0,0]

K = int(input())
W, H = map(int, input().split())
graph = []
queue = deque()
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
for x in range(H):
    graph.append(list(map(int, input().split())))

queue.append((0, 0))
visited[0][0] = 1


def bfs():
    while queue:
        a,b = queue.popleft()