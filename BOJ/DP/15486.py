import sys
input = sys.stdin.readline

t = []
p = []
N = int(input())
dp = [0] * (N+1)

for i in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

res = 0
for i in range(N):
    res = max(res, dp[i])
    if i + t[i] > N:
        continue
    dp[i + t[i]] = max(res + p[i], dp[i + t[i]])
print(max(dp))