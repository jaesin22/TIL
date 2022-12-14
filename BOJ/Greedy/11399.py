N = int(input())
A = list(map(int, input().split()))

A.sort()

cnt = A[0]
for i in range(1, N):
    A[i] = A[i] + A[i-1]
    cnt += A[i]

print(cnt)
