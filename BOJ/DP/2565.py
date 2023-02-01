import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = [1] * (N + 1)
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[0], x[1]))

for i in range(1, N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))