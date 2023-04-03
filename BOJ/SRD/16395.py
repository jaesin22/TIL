
N, K = map(int, input().split())

graph = [[0] * 30 for _ in range(30)]
graph[0][0] = 1
graph[1][0] = 1
graph[1][1] = 1
for i in range(2, 30):
    for j in range(i+1):
        if j == 0:
            graph[i][j] = 1
        if j == i:
            graph[i][j] = 1
        
        graph[i][j] = graph[i-1][j-1] + graph[i-1][j]
    

print(graph[N-1][K-1])