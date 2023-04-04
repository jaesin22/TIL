import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0] * (N)
    dp[0] = A[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1] + A[i], A[i])

    print(max(dp))

