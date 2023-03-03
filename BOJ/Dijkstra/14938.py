import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    distance = [INF] * (N+1)
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)
        if dist > distance[curr]:
            continue


        for next, weight in graph[curr]:
            cost = dist + weight
            if cost > M:
                continue

            if cost < distance[next]:
                distance[next] = cost
                prev[next] = curr
                heapq.heappush(queue, (cost, next))
    return distance

N, M, R = map(int, input().split())
T = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
prev = [0] * (N+1)
for i in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

ans = []
for i in range(1, N+1):
    res = dijkstra(i)
    cnt = 0
    for i in range(len(res)):
        if res[i] != INF:
            cnt += T[i]
    ans.append(cnt)    
    cnt = 0

print(max(ans))

