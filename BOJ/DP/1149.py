import sys
input = sys.stdin.readline

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, len(dp)):
    # 이번 케이스에서 집을 0번 색으로 칠했을 때의 비용은, 이번에 0번으로 칠하는데 드는 비용 + 이전 케이스에서 1번색/ 2번색으로 칠했던 경우의 비용의 합이다.
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    # 위와 마찬가지, 집을 1번 색으로 칠했을 때의 비용은, 이번에 1번으로 칠하는데 드는 비용 + 이전 케이스에서 0번색/ 2번색으로 칠했던 경우의 비용의 합
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    # 결국 memo 리스트는 i번째 집까지를 0,1,2번 색으로 칠했을때의 최소값을 나타내는 리스트가 된다.
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

# 그렇기 때문에, 마지막 값의 최소값을 출력해주면, 여태까지 누적되었던 색칠 비용의 최솟값이랑 동일하다.
# n-1이 마지막인걸 기억
print(min(dp[N-1]))