import sys
N = int(input())
A = list(map(int, input().split()))
res = []
for i in range(N):
    cnt = 0
    curr = A[i]
    for j in range(N):
        cnt += abs(A[j] - A[i])
    res.append((A[i], cnt))

res.sort(key=lambda x: (x[1], x[0]))

print(res[0][0])