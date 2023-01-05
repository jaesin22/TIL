N, M = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0,0
count = 0
hap = A[0]
while start < N and end < N:
    if hap == M:
        count += 1
        hap -= A[start]
        start += 1
    elif hap > M:
        hap -= A[start]
        if start < N:
            start += 1
    else:
        end += 1
        if end < N:
            hap += A[end]

print(count)
