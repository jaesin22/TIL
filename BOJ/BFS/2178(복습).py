from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = [[0, 0]]
graph[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == "1":
            queue.append((nx, ny))
            graph[nx][ny] = graph[a][b] + 1
# 0, 0부터 bfs를 이용해 동, 서, 남, 북을 검사하여 "1"인 값을 찾는다.
# 만약 "1"이라면 기준이 되는 숫자에 +1을 하여 값을 넣어준다.
# 이렇게 쭉 검사를 해나가면 마지막 s[n - 1, m - 1]에는 최솟값이 들어가게 된다.
print(graph[N-1][M-1]) # graph의 끝에 있는 값 출력