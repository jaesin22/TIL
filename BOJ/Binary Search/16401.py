import sys
input = sys.stdin.readline
m, n = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)
result = 0
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        result = 0
        break
    
    cnt = 0
    for i in arr:
        cnt += i // mid

    if cnt >= m:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1

print(result)