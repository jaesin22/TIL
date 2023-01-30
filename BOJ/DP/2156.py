import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

if N == 1 or N == 2:
    print(sum(arr))
    sys.exit()

dp = [0] * (N + 1)
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])

print(dp[N-1])