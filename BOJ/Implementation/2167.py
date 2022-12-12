N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


K = int(input())
for j in range(K):
    count = 0
    A = list(map(int, input().split()))
    for i in range(A[0]-1, A[2]):
        for j in range(A[1]-1, A[3]):
            count += graph[i][j]
    print(count)