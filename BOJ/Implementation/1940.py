N = int(input())
M = int(input())

A = list(map(int, input().split()))

start, end = 0, N-1
cnt = 0
A.sort()
while start < end:
    hap = A[start] + A[end]

    if hap == M:
        cnt += 1
        start += 1
        end -= 1

    elif hap < M:
        start += 1

    else:
        end -= 1

print(cnt)