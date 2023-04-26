N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

arr = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for l in range(M):
            arr[i][j] += A[i][l]* B[l][j]

for i in arr:
        print(*i)