import sys

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

# dfs 이용해 각 바이러스 사방으로 퍼트리기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고 다시 재귀적으로 수행
                visited[nx][ny] = 2
                virus(nx, ny)


# 현재 맵에서 안전 영역 크기 계산하는 메소드
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                score += 1
    return score

# dfs를 이용해 울타리 설치하며 매 번 안전영역 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(N):
            for j in range(M):
                visited[i][j] = graph[i][j]
        # 각 바이러스 위치에서 전파 진행
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)