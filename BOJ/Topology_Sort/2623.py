import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    res = []
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        curr = queue.popleft()
        res.append(curr)

        for i in graph[curr]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)
    if len(res) != N:
        print(0)
    else:
        for i in res:
            print(i)

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
# 방향 그래프의 모든 간선 정보 입력 받기
for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        graph[arr[i]].append(arr[i + 1])
        indegree[arr[i + 1]] += 1

topology_sort()