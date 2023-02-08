import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

A = list(map(int, input().split()))
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))

maxdp = max(dp)
res = []
for i in range(N-1, -1, -1):
    if dp[i] == maxdp:
        res.append(A[i])
        maxdp -= 1
res.sort()
print(*res)