N = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
graph = [list(input()) for _ in range(N)]

def count():
    row_cnt, col_cnt, max_row, max_col = 1, 1, -1, -1
    # 행
    for i in range(N):
        for j in range(N-1):
            if graph[i][j] == graph[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            max_row = max(max_row, row_cnt)
        row_cnt = 1
    # 열
    for j in range(N):
        for i in range(N-1):
            if graph[i][j] == graph[i+1][j]:
                col_cnt += 1
            else:
                col_cnt = 1

            max_col = max(max_col, col_cnt)
        col_cnt = 1

    ans = max(max_row, max_col) 
    return ans


res = 0

for i in range(N):
    for j in range(N):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[i][j] != graph[nx][ny]:
                    graph[nx][ny], graph[i][j] = graph[i][j], graph[nx][ny]

                    res = max(res, count())
                    graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]


print(res)