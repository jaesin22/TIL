import sys
from collections import deque
input = sys.stdin.readline
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,1,-1]
shark_dx = [0,0,-1,1]
shark_dy = [-1,1,0,0]
graph = [[0] * 4 for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]

def copy(fish):
    for i in fish:
        fish.append(i)

    return fish

def chk_smell(smell):
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

    return smell
 
def move(queue):
    while queue:
        a, b, c = queue.popleft()
        nx = a + dx[c]
        ny = b + dy[c]

        if 0 <= nx < 4 and 0 <= ny < 4: # 격자의 범위 체크
            if smell[nx][ny] == 0: # 물고기의 냄새 체크
                if graph[nx][ny] != 'S': # 상어 체크
                    return
                
                else:
                    for i in range(8):
                        nx = a + dx[i]
                        ny = b + dy[i]

                        if 0 <= nx < 4 and 0 <= ny < 4: # 격자의 범위 체크
                            if smell[nx][ny] == 0: # 물고기의 냄새 체크
                                if graph[nx][ny] != 'S': # 상어 체크
                                    graph[a][b] = 0
                                    graph[nx][ny] = 1




M, S = map(int, input().split())
fish = deque()
for i in range(M):
    fx, fy, d = map(int, input().split())
    fish.append((fx-1, fy-1, d-1))
prev_fish = copy(fish)
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
