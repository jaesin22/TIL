N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] # dp[자리 수][0] = dp[자리 수 - 1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8] # 9 뒤에는 오직 숫자 8만이 올 수 있음
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] # 전의 값과 그 다음 값

print(sum(dp[N]) % 1000000000)