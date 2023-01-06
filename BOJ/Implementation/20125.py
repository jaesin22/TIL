import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def find_heart(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == '*':
            cnt += 1
        else:
            return False
    if cnt == 4:
        return True

def left_arm(x, y):
    cnt = 0
    while True:
        if graph[x][y-1] == '*':
            cnt += 1
            y = y-1
        else:
            break
    return cnt

def right_arm(x, y):
    cnt = 0
    while True:
        if graph[x][y+1] == '*':
            cnt += 1
            y = y+1
        else:
            break
    return cnt

def waist(x, y):
    cnt = 0
    while True:
        if graph[x+1][y] == '*':
            cnt += 1
            x = x+1
        else:
            break
    return [cnt, x, y]

def left_leg(x, y):
    cnt = 0
    while x+1 < N and y < N:
        if graph[x+1][y-1] == '*':
            cnt += 1
            x = x + 1
        else:
            break
    
    return cnt

def right_leg(x, y):
    cnt = 0
    while x+1 < N and y+1 < N:
        if x >= N and y >= N:
            break
        if graph[x+1][y+1] == '*':
            cnt += 1
            x = x+1
        else:
            break
    return cnt


N = int(input())
graph = []
x, y = 0, 0
for i in range(N):
    graph.append(input())

for i in range(N):
    for j in range(N):
        if graph[i][j] == '*':
            chk = find_heart(i, j)
            if chk == True:
                x, y = i, j

print(x+1, y+1)
A = waist(x, y) # 허리 위치, 다리 길이 구해야 되서 가져옴
print(left_arm(x, y), right_arm(x, y), A[0], left_leg(A[1], A[2]), right_leg(A[1], A[2]))