import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    queue = []
    distance = [INF] * (N+1)
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, curr = heapq.heappop(queue)

        if dist > distance[curr]:
            continue

        for next, weight in graph[curr]:
            cost = dist + weight
            if H[next] > H[curr]: 
                if cost < distance[next]:
                    distance[next] = cost
                    prev[next] = curr
                    heapq.heappush(queue, (cost, next))

    return distance


N, M, D, E = map(int, input().split())
H = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
prev = [0] * (N+1)
for i in range(M):
    a, b, n = map(int, input().split())
    graph[a].append((b, n))
    graph[b].append((a, n))

one_dijkstra = dijkstra(1)
N_dijkstra = dijkstra(N)

res = []
for i in range(1, N+1):
    if one_dijkstra[i] != INF and N_dijkstra[i] != INF:
        # (얻은 성취감) - (소모한 체력)을 배열에 넣음
        res.append(H[i] * E - D * (one_dijkstra[i] + N_dijkstra[i]))

if len(res) == 0:
    print("Impossible")
else:
    print(max(res))