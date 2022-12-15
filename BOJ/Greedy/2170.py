import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x:(x[0],x[1]))
cnt = 0
start, end = arr[0][0], arr[0][1]

for i in range(len(arr)-1) : 
    if end < arr[i+1][0]:
        cnt += end-start
        start = arr[i+1][0]
        end = arr[i+1][1]
    if end >= arr[i+1][0]:
        if end < arr[i+1][1]:
            end = arr[i+1][1]

cnt+=end-start
print(cnt)