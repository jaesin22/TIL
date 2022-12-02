import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

INF = 100000 #임의의 큰 수

def bfs(queue, blanks):
    visited = [[0] * N for _ in range(N)]

    time = 0
    while True:
        length = len(queue) # 바이러스의 개수 
        if blanks == 0 or length == 0:
            if blanks == 0: #옵션 1 모든 빈 칸에 바이러스를 퍼트리면 종료
                return time 
            else: # 옵션 2  바이러스를 어떻게 놓아도 전체에 퍼트릴 수 없는 경우
                return INF
        
        time += 1
        for i in range(length): # 큐 길이 만큼 반복해주는 for문이 이 문제 해 결의 핵심
            a, b = queue.popleft()
            if visited[a][b] == 0:
                visited[a][b] = 1
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == 0: #방문하지 않은 칸에 대해
                        if graph[nx][ny] == 0: # 빈칸인 경우
                            queue.append((nx, ny))
                            visited[nx][ny] = 1
                            blanks -= 1

N, M = map(int, input().split())
graph = []
for x in range(N):
    graph.append(list(map(int, input().split())))

virus_pos = [] # 바이러스 위치 정보 저장
black_cnt = 0 #빈칸 개수 저장

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_pos.append((i, j))
        elif graph[i][j] == 0:
            black_cnt += 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 활성 바이러스를 만들기 위한 조합(combination) 사용
virus_combi = combinations(virus_pos, M)
res = INF

for virus_list in virus_combi:
    queue = deque()
    for virus in virus_list:
        queue.append(virus)

    tmp = bfs(queue, black_cnt)
    res = min(res, tmp)

if res == INF: # 옵션 2 바이러스를 어떻게 놓아도 전체에 퍼트릴 수 없는 경우
    print(-1)
else: 
    print(res)