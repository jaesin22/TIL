import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

dp[1] = 1

for x in range(2, N+1):
    dp[x] = dp[x-1] + dp[x-2]

print(dp[N])