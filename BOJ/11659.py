import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

sum = [0] * (N+1)

for i in range(N):
    sum[i] = sum[i-1] + num[i]

for y in range(M):
    a, b = map(int, input().split())
    print(sum[b-1] - sum[a-2])
