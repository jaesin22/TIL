import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    connet = deque() # 국경선을 공유한 곳의 지역을 담을 큐
    people, count = 0, 0 # 한 지역에 대해 국경선 공유할 때 연합인구수와 연합을 이루고 있는 국가 수를 저장하기 위해 count, people 변수 이용
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()
        connet.append((a, b)) # queue에 존재할 때 까지 connet queue에 국경선을 공유하여 연합한 국가들의 위치를 append, 
        count += 1 # 연합인구수(people)에 graph[a][b]를 더하고 연합을 이루고 있는 국가 수(count)를 + 1 증가시켜줌
        people += graph[a][b]
        for i in range(4): # 4방향을 돌면서 인접한 국가들과의 인구 수 차이(diff)를 계산하여 만약 diff가 주어진 L 이상, 
            nx = a + dx[i] # R 이하라면 국경선을 공유하기 위하여 visited에 count를 넣어서 방문처리 해주고, queue에 국경선을 공유한 위치(nx, ny)를 append
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    diff = abs(graph[a][b] - graph[nx][ny])
                    if L <= diff <= R:
                        visited[nx][ny] = count
                        queue.append((nx, ny))
    while connet: # 국경선이 공유되는지 queue를 통해서 다 확인한 후에 위에서 구한 connet 큐에서 
        x, y = connet.popleft() # 국경선을 공유한 지역에 연합인구수 // 연합을 이루고 있는 개수로 garph 값을 변경시켜줌
        graph[x][y] = (people // count)

    if count == 1: # bfs를 돌면서 count 즉, 국경선을 공유한 지역이 없다면 return 0
        return 0
    return 1 # bfs를 돌면서 count 즉, 국경선을 공유한 지역이 있다면 return 1
 
answer = 0
while True:
    #  while 문을 돌면서 방문하지 않은 곳을 q에 append 해주고 모든 지역에 bfs를 돌려서 break_cnt(국경선을 공유한 국가)가 0, 
    #  즉 모든 지역이 국경선을 공유하지 않았다면 while을 빠져나가게 하고 만약 국경선을 공유한 국가가 있다면 answer +1 증가 시켜줌
    queue = deque()
    break_cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue.append((i, j)) # 전체 나라 탐색을 위해 전체 나라 넣음
                break_cnt += bfs(i, j)
    if break_cnt == 0:
        break
    else:
        answer += 1

print(answer)