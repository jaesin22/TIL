import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))


res = 0
chk = min(N, M)
for k in range(chk):
    for i in range(N - k):
        for j in range(M - k):
            if graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]:
                res = max(res, (k+1) ** 2)

print(res)