N = int(input())
dp = [[0] * 3 for _ in range(N+1)]

for i in range(3):
    dp[1][i] = 1 

for j in range(2, N + 1):
    dp[j][0] = dp[j-1][1] + dp[j-1][2] % 9901
    dp[j][1] = dp[j-1][0] + dp[j-1][2] % 9901
    dp[j][2] = dp[j-1][0] + dp[j-1][1] + dp[j-1][2] % 9901

print(sum(dp[N]) % 9901)