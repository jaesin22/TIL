import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

for x in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    num = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)

res = []

for i in range(1, N + 1):
    res.append(bfs(graph, i))

print(res.index(min(res)) + 1)