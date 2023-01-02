import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

result = float('inf')
ans = [float('inf'), float('inf')]
start, end = 0, len(A) - 1
while start < end:

    if abs(A[start] + A[end]) < result:
        result = abs(A[start] + A[end])
        ans = [A[start],  A[end]]

    if A[start] + A[end] < 0:
        start += 1
    else:
        end -= 1


print(*ans)
