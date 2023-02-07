import sys
input = sys.stdin.readline

C, N = map(int, input().split())
wt, val = [], []

for _ in range(N):
    a, b = map(int, input().split())
    wt.append(a)
    val.append(b)

dp = [[0] * (C+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(C+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][C])