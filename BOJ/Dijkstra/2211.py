import sys
import  heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):    
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)

        if distance[curr] < dist:
            continue

        for next, weight in graph[curr]:
            cost = weight + dist
            if cost < distance[next]:
                distance[next] = cost
                prev[next] = curr
                heapq.heappush(queue, (cost, next))                                                                                                                                              

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    # 양방향 그래프일 땐 이렇게 하자 !!
    u, m, v  = map(int, input().split())
    graph[u].append((m, v))
    graph[m].append((u, v))

distance = [INF] * (N+1)
prev = [0] * (N+1)

dijkstra(1)
print(N-1)
for i in range(2, N+1): # 1번 정점을 제외함
    print(i, prev[i]) #i = 각 정점 U, prev[i]는 모르겠다.. 뭘까..