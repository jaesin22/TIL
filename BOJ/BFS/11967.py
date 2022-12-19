import sys
from collections import deque, defaultdict
input = sys.stdin.readline


dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    cnt = 1
    graph = [[0] * N for _ in range(N)] # 불 켠 방 표시
    visited = [[0] * N for _ in range(N)] # 방문 표시
    visited[0][0] = 1
    graph[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        a, b = queue.popleft()
        for tr, tc in turnInfo[(a, b)]: # 불켤 수 있는 곳(딕셔너리 참조)
            if not graph[tr][tc]:
                graph[tr][tc] = 1 # 새로 불 켜기
                cnt += 1
                for i in range(4):  # 4방향 연결된 곳
                    nx = tr + dx[i]
                    ny = tc + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if visited[nx][ny] != 0: # 방문한 적 있으면(새로 연결되어 또 불을 켤 곳이 있을 수 있으므로)
                            queue.append((nx, ny)) # 큐에 담기
        
        # 현 위치 기준으로
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 첫 방문인데 이미 불 켜진 곳이면
                if not visited[nx][ny] and graph[nx][ny]:
                    queue.append((nx, ny)) # 재검사를 위해 큐에 담기
                    visited[nx][ny] = 1 # 방문 표시
    
    return cnt


N, M = map(int, input().split())
turnInfo = defaultdict(list) # 각 위치에서 불 켤 수 있는 위치 정보 저장

for _ in range(M):
    sr, sc, tr, tc = map(int, input().split())
    turnInfo[(sr-1, sc-1)].append((tr-1, tc-1))

print(bfs())