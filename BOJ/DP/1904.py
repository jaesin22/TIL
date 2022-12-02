import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * 1000001
dp[0] = 1
dp[1] = 1
for x in range(2, 1000001):
    dp[x] = dp[x-1] + dp[x-2]
    if dp[x] >= 15746:
        dp[x] = dp[x] % 15746

print(dp[N])