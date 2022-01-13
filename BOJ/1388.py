N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))


cnt = 0
for i in range(N):
    token = '1'
    for j in range(M):
        if graph[i][j] == '-':
            if graph[i][j] != token:
                cnt += 1
        token = graph[i][j]


for i in range(M):
    token = '1'
    for j in range(N):
        if graph[j][i] == '|':
            if graph[j][i] != token:
                cnt += 1
        token = graph[j][i]
    

print(cnt)