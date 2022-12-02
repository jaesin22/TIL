import sys
from collections import deque
input = sys.stdin.readline


# 1. 공기와 접촉하면 천천히 녹는다. 내부에 있는 공간은 접촉하지 않는 것으로 가정한다. 이 의미에 힌트가있다. 

# 2. 내부에 있는 공간은 접촉하지 않으므로 외부에서부터 BFS로 진행해줘서 2번이상 접촉을하면 다음 반복문에서 제외시켜주면된다.

# 3. 마지막으로 전체가 0 일시 무한루프 탈출해준다.

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0
while True:
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] >= 1 and visited[nx][ny] == 0: #여기서 방문 처리를 안하는 이유는 방문 처리를 해버리면 1번밖에 방문을 못해서 외부 공기 2번 이상 접촉 여부 확인 불가
                    graph[nx][ny] += 1

                elif graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        
    
    res = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
            elif graph[i][j] > 0:
                graph[i][j] = 1
                res = 1
    
    cnt += 1
    if res == 0:
        print(cnt)
        break

            
    
    
