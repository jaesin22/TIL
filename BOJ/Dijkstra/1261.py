import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dijkstra():
    distance[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))

    while queue:
        dist, curr_x, curr_y = heapq.heappop(queue)

        if curr_x == N-1 and curr_y == M-1:
            print(distance[curr_x][curr_y])
            break
    
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, nx, ny))


M, N = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

distance = [[INF] * M for _ in range(N)]

dijkstra()