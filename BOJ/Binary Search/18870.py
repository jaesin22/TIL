import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

A = sorted(list(set(arr)))

for i in arr:
    start, end = 0, len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == i:
            print(mid, end = ' ')
            break
        elif A[mid] < i:
            start = mid + 1
        else:
            end = mid - 1