N, M = map(int, input().split())

items = list(map(int, input().split()))

sum = [0] * (N+1)
for i in range(N):
    sum[i] = sum[i-1] + items[i]

for x in range(M):
    i, j = map(int, input().split())
    print(sum[j-1] - sum[i-2])

    