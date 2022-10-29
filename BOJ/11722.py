import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * N
A = list(map(int, input().split()))

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))