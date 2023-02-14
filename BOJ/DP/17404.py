import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

INF = float('inf')
res = INF

for i in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][i] = graph[0][i]
    for j in range(1, N):
        dp[j][0] = graph[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = graph[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = graph[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            res = min(res, dp[-1][j])

print(res)