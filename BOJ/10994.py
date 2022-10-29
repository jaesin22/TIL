import sys
N = int(sys.stdin.readline())
dp = [0] * 46
dp[0] = 0
dp[1] = 1
dp[2] = 1

for x in range(3, N+1):
    dp[x] = dp[x-2] + dp[x-1]

print(dp[N])