import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
start, end = 0, 1

result = float('inf')

while start < N and end < N:
    tmp = arr[end] - arr[start]
    if tmp == M:
        result = tmp
        break
    elif tmp > M:
        result = min(result, tmp)
        start += 1
    else:
        end += 1

print(result)