import sys
input = sys.stdin.readline
N = int(input())

res = [0] * 1001
res[1] = 1
res[2] = 3
for x in range(3, N+1):
    res[x] = res[x-2] * 2 + res[x-1] # 점화식 (N-2) * 2 + (N+1)

print(res[N]%10007)