import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dijkstra():
    global cnt
    queue = []
    distance[0][0] = 0
    heapq.heappush(queue, (graph[0][0], 0, 0))
    while queue:
        dist, curr_x, curr_y = heapq.heappop(queue)

        if curr_x == N-1 and curr_y == N-1:
            return distance[curr_x][curr_y]
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, nx, ny))

cnt = 1
while True:
    N = int(input())
    distance = [[INF] * (N) for _ in range(N)]
    if N == 0:
        sys.exit()
    
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    
    res = dijkstra()
    print("Problem " + str(cnt) + ": " + str(res))
    cnt += 1

    
