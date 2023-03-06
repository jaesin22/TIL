from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    res = []
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()
        print(curr)
        res.append(curr)

        for i in graph[curr]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in res:
        print(i, end =' ')

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()