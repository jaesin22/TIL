import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
wt = []
val = []

for _ in range(N):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)

for i in range(N + 1):
    for j in range(K + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])