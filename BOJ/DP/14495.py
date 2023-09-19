
N = int(input())
dp = [0] * (N+3)

dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-3]

print(dp[N-1])