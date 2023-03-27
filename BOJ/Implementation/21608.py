import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
board = [[0] * N for _ in range(N)]
graph = []
for _ in range(N**2):
    graph.append(list(map(int, input().split())))

for student in graph:
    number = student[0]
    position = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                like, blank = 0, 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if board[nx][ny] in student[1:]:
                        like += 1
                    if board[nx][ny] == 0:
                        blank += 1

                
                position.append([like, blank, i, j])

    position.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))
    board[position[0][2]][position[0][3]] = number


res = 0
graph.sort() # 학생들의 번호에 맞춰서 탐색하기 위해 학생 번호를 기준으로 정렬
for i in range(N):
    for j in range(N):
        cnt = 0
        num = board[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if board[nx][ny] in graph[num-1][1:]:
                cnt += 1

        if cnt != 0:
            res += (10 ** (cnt - 1))

print(res) 