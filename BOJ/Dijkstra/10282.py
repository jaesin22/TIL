import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    global cnt
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)
        for next, weight in graph[curr]:
            cost = dist + weight

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))

    return distance

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    cnt = 0
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    for i in range(D):
        a, b, c = map(int, input().split())
        graph[b].append((a, c))
    
    res = dijkstra(C)
    max_res = 0
    cnt = 0
    for i in res:
        if i != INF:
            if max_res < i:
                max_res = i
            cnt += 1
    print(cnt, max_res)
    
