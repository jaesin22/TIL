import sys
input = sys.stdin.readline
N = int(input())
dp = []

for x in range(N):
    dp.append(list(map(int, input().split())))

k = 2
for i in range(1, N):
    for j in range(i+1): # i+1을 하는 이유는 i번째줄보다 j번째 줄이 하나 더 많기 때문
        if j == 0: #왼쪽 가장자리
            dp[i][j] = dp[i-1][j] + dp[i][j]
        
        elif j == i: # 오른쪽 끝
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        
        else: # 그외에 중간
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
        
    k += 1

print(max(dp[N-1]))