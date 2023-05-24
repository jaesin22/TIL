graph = [[0] * 15 for _ in range(5)]

res = ''
for i in range(5):
    A = list(input())
    for j in range(len(A)):
        graph[i][j] = A[j]

for i in range(15):
    for j in range(5):
        if graph[j][i] != 0:
            print(graph[j][i], end='')