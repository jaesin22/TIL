import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))
res = float('inf')
start, end = 0,0
cnt = A[0]
while start < N or end < N:
    if cnt >= S:
        cnt -= A[start]
        res = min(res, end - start + 1)
        start += 1
    else:
        end += 1
        if end == N:
            break
        cnt += A[end]
if res == float('inf'):
    print(0)
else:
    print(res)