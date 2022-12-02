import sys
input = sys.stdin.readline
N = int(input())
dp = []

for x in range(N):
    dp.append(list(map(int, input().split())))

k = 2
for i in range(1, N):
    for j in range(k):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
        
    k += 1

print(max(dp[N-1]))