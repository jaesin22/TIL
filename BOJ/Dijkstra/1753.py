import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] > dist:
            continue
#         -- for i in graph[꺼낸노드번호]:
#   꺼낸노드번호에서 갈수 있는 노드와 거리정보를 i를 통해 한개씩 접근
#    >> i[0] : 현재 노드에서 갈 수 있는 노드 번호

#    >> i[1] : 현재 노드에서 갈 수 있는 노드 번호까지의 거리
# i[0]까지의 최소비용(cost)은 >>> 현재 노드의 최소비용(dist) + i[1]  이다.
# 만약에 cost값이 최단 거리 테이블의 거리정보보다 작으면, 업데이트 해주고 힙큐에 정보를 넣어준다. 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

V, E = map(int, input().split())

start_node = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

# 연결 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start_node)

# i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    