N = int(input())
K = int(input())
graph = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
arr = []
L = int(input())
for _ in range(L):
    x, y = map(str, input().split())
    arr.append([int(x), y])
