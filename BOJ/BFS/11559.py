import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph = []
for i in range(12):
    graph.append(list(input().rstrip()))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    temp.append((x, y))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    temp.append((nx, ny))
                    visited[nx][ny] = 1


# 맨 아래칸부터 위로 올라가면서 하나씩 땡기는 함수
def down():
    for i in range(6): # 줄이 여섯개니까 6번 반복
        for j in range(10, -1, -1): # 맨 아래칸 바로 위
            for k in range(11, j, -1): # 맨 아래칸 부터
                if graph[j][i] != '.' and graph[k][i] == '.':
                    graph[k][i] = graph[j][i]
                    graph[j][i] = '.'
                    break


def delete(temp):
    for a, b in temp:
        graph[a][b] = '.'

res = 0
while True:
    flag = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                temp = []
                bfs(i, j)
                # 4칸 확인
                if len(temp) >= 4:
                    flag = 1
                    delete(temp)
    
    if flag == 0:
        break
    down()
    res += 1

print(res)