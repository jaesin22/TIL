import sys
input = sys.stdin.readline

arr = [0] * 1001
N, C = map(int, input().split())
graph = list(map(int ,input().split()))

for x in graph:
    print(x)
    arr[x] += 1

for y in arr:
    if y != 0:
        print(y, end=' ')