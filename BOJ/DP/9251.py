M = ' ' + input()
N = ' ' + input()

dp = [[0] * len(N) for _ in range(len(M))]
for i in range(1, len(M)):
    for j in range(1, len(N)):
        if M[i] == N[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])