import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    queue = []
    distance = [INF] * (N+1)
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)
        if dist > distance[curr]:
            continue
        
        for next, weight in graph[curr]:
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))
    return distance

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    K = int(input())
    A = list(map(int, input().split()))
    
    for i in A:
        res = dijkstra(i)
        for j in range(len(res)):
            arr[j] += res[j]

    print(arr.index(min(arr)))