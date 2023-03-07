import sys
import heapq
input = sys.stdin.readline

def topology_sort():
    queue = []
    res = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    while queue:
        curr = heapq.heappop(queue)
        res.append(curr)

        for i in graph[curr]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(queue, i)
    
    for i in res:
        print(i, end=' ')


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()